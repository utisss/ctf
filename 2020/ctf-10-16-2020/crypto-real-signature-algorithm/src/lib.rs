use std::{
	error::Error,
	fmt::{self, Display, Formatter},
	str::FromStr,
};

use ramp::{int::Int, traits::Integer};
use tokio::{
	io::{AsyncBufReadExt, AsyncRead, AsyncWriteExt, BufReader},
	net::TcpStream,
	time,
	time::Duration,
};

pub use config::{Config, ConfigBuilder};

pub mod config;
pub mod env;
pub mod errors;

// I think there's a bug in Clippy
// Lifetimes need to be explicit here
#[allow(clippy::needless_lifetimes)]
async fn trimmed_read_line<'a, T>(
	stream: &mut T,
	buf: &'a mut String,
	config: &Config<'_>,
) -> Result<&'a str, tokio::io::Error>
where
	T: AsyncBufReadExt + Unpin,
{
	buf.clear();
	let size = time::timeout(
		Duration::from_secs(config.read_timeout()),
		stream.read_line(buf),
	)
	.await??;
	Ok(&buf[..size].trim())
}

async fn write_line<'a, T>(stream: &mut T, buf: &str) -> Result<(), tokio::io::Error>
where T: AsyncBufReadExt + Unpin + AsyncWriteExt {
	stream.write_all(format!("{}\n", buf).as_bytes()).await?;
	Ok(())
}

#[derive(Debug)]
enum MenuSelectionError {
	BadSelection,
	LockedFeature,
	IoError(tokio::io::Error),
}

impl Error for MenuSelectionError {}

impl Display for MenuSelectionError {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		match self {
			Self::BadSelection => write!(f, "Invalid selection."),
			Self::LockedFeature => write!(f, "This selection has been locked."),
			Self::IoError(err) => write!(f, "{}", err),
		}
	}
}

enum MenuSelections {
	SignMessage = 1,
	VerifySignature = 2,
}

struct Menu {
	sign_counter: u8,
	verify_counter: u8,
}

impl FromStr for MenuSelections {
	type Err = MenuSelectionError;

	fn from_str(s: &str) -> Result<Self, Self::Err> {
		let num: u8 = s.parse().map_err(|_| MenuSelectionError::BadSelection)?;
		match num {
			x if x == Self::SignMessage as u8 => Ok(Self::SignMessage),
			x if x == Self::VerifySignature as u8 => Ok(Self::VerifySignature),
			_ => Err(MenuSelectionError::BadSelection),
		}
	}
}

impl From<tokio::io::Error> for MenuSelectionError {
	fn from(err: tokio::io::Error) -> Self { MenuSelectionError::IoError(err) }
}

impl Menu {
	pub fn new(config: &Config<'_>) -> Self {
		Self {
			verify_counter: config.verify_tries(),
			sign_counter: config.sign_tries(),
		}
	}

	pub async fn enter<T>(
		&mut self,
		stream: &mut BufReader<T>,
		line: &mut String,
		config: &Config<'_>,
	) -> Result<MenuSelections, MenuSelectionError>
	where
		T: AsyncRead + Unpin + AsyncWriteExt,
	{
		write_line(stream, "Select option:").await?;
		write_line(stream, "[1] Sign").await?;
		write_line(stream, "[2] Flag").await?;

		let line = trimmed_read_line(stream, line, config).await?;
		let selection = line.parse::<MenuSelections>()?;
		match selection {
			MenuSelections::VerifySignature => {
				if self.verify_counter == 0 {
					write_line(stream, "").await?;
					Err(MenuSelectionError::LockedFeature)
				} else {
					self.verify_counter -= 1;
					Ok(selection)
				}
			},
			MenuSelections::SignMessage => {
				if self.sign_counter == 0 {
					Err(MenuSelectionError::LockedFeature)
				} else {
					self.sign_counter -= 1;
					Ok(selection)
				}
			},
		}
	}
}

async fn verify<T>(
	stream: &mut BufReader<T>,
	line: &mut String,
	config: &Config<'_>,
	e: &Int,
	n: &Int,
	challenge: &Int,
) -> Result<(), tokio::io::Error>
where
	T: AsyncRead + Unpin + AsyncWriteExt,
{
	loop {
		write_line(stream, "Enter signature.").await?;
		let line = trimmed_read_line(stream, line, config).await?;
		let m = &match Int::from_str_radix(line, 10) {
			Ok(line) => line,
			Err(_) => {
				write_line(stream, "Bad encoding.").await?;
				continue;
			},
		};

		if m >= n {
			write_line(stream, "Input value is too large.").await?;
			continue;
		}

		let to_verify = &m.pow_mod(e, n);
		// No guarantee of constant time
		if challenge == to_verify {
			write_line(stream, &format!("Success! The flag is {}.", config.flag())).await?;
			stream.shutdown().await?;
			break Ok(());
		} else {
			write_line(stream, "Wrong! Bad signature.").await?;
			break Ok(());
		}
	}
}

async fn sign<T>(
	stream: &mut BufReader<T>,
	line: &mut String,
	config: &Config<'_>,
	d: &Int,
	n: &Int,
	challenge: &Int,
) -> Result<(), tokio::io::Error>
where
	T: AsyncRead + Unpin + AsyncWriteExt,
{
	loop {
		write_line(stream, "Enter challenge.").await?;
		let line = trimmed_read_line(stream, line, config).await?;
		let m = &match Int::from_str_radix(line, 10) {
			Ok(line) => line,
			Err(_) => {
				write_line(stream, "Bad encoding.").await?;
				continue;
			},
		};

		if m >= n {
			write_line(stream, "Input value is too large.").await?;
			continue;
		}

		// No guarantee of constant time
		if challenge == m {
			write_line(stream, "This value will not be signed. It is forbidden.").await?;
			continue;
		}

		let tag = &m.pow_mod(d, n);
		write_line(
			stream,
			&format!("The signature is {}.", tag.to_str_radix(10, false)),
		)
		.await?;
		break Ok(());
	}
}

struct KeyPair {
	e: Int,
	d: Int,
	n: Int,
}

impl KeyPair {
	const E: u128 = (1 << 16) + 1;

	#[allow(clippy::many_single_char_names)]
	pub fn generate(config: &Config<'_>) -> Self {
		let e = Int::from(Self::E);
		let p = &ramp_primes::Generator::new_prime(config.bits() / 2);
		let q = &ramp_primes::Generator::new_prime(config.bits() / 2);
		let n = p * q;
		let p_dec = &(p - 1);
		let q_dec = &(q - 1);
		let carmichael_totient = &Int::lcm(p_dec, q_dec);
		let d = Int::extended_gcd(carmichael_totient, &e).y;
		let d = d + carmichael_totient;
		let d = d.mod_floor(carmichael_totient);

		Self { e, d, n }
	}
}

async fn internal_process<T>(
	stream: &mut BufReader<T>,
	config: &Config<'_>,
) -> Result<(), Box<dyn Error>>
where
	T: AsyncRead + Unpin + AsyncWriteExt,
{
	let line = &mut String::new();

	write_line(stream, "Loading challenge...").await?;
	let key_pair = KeyPair::generate(config);
	let challenge = &ramp_primes::Generator::new_composite(config.bits() / 2);

	write_line(
		stream,
		"This service generates RSA signatures. Get the flag by signing the challenge.",
	)
	.await?;
	write_line(
		stream,
		&format!(
			"Only {} messages will be signed. Validation attempts are limited to {} tries.",
			config.sign_tries(),
			config.verify_tries()
		),
	)
	.await?;
	write_line(
		stream,
		&format!(
			"Sign {} to access the flag.",
			challenge.to_str_radix(10, false)
		),
	)
	.await?;
	write_line(
		stream,
		&format!(
			"The public modulus is {}.",
			&key_pair.n.to_str_radix(10, false)
		),
	)
	.await?;
	write_line(
		stream,
		&format!(
			"The public exponent is {}.",
			&key_pair.e.to_str_radix(10, false)
		),
	)
	.await?;

	let mut menu = Menu::new(config);

	loop {
		match menu.enter(stream, line, config).await {
			Ok(selection) => {
				match selection {
					MenuSelections::SignMessage => {
						sign(stream, line, config, &key_pair.d, &key_pair.n, challenge).await?
					},
					MenuSelections::VerifySignature => {
						verify(stream, line, config, &key_pair.e, &key_pair.n, challenge).await?
					},
				}
			},
			Err(err) => {
				match err {
					MenuSelectionError::IoError(err) => return Err(err.into()),
					_ => {
						write_line(stream, &format!("{}", err)).await?;
					},
				}
			},
		}
	}
}

pub async fn process(stream: TcpStream, config: &Config<'_>) {
	let mut stream = BufReader::new(stream);

	if let Err(_err) = internal_process(&mut stream, config).await {
		#[cfg(debug_assertions)]
		eprintln!("{}", _err);
	}
}
