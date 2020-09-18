use std::error::Error;

use so::randombytes;
use sodiumoxide as so;
use tokio::{
	io::{AsyncBufReadExt, AsyncWriteExt, BufReader},
	net::TcpStream,
	time,
	time::Duration,
};

pub use config::{Config, ConfigBuilder};

pub mod config;
pub mod env;
pub mod errors;

const STANDARD_DELAY: u64 = 1;
const NO_DELAY: u64 = 0;
const DOTS: u8 = 3;

macro_rules! write_all_delay {
	($stream:ident, $delay:expr, $message:expr $(, $items:expr)*) => {
		$stream.write_all(format!($message, $($items,)*).as_bytes()).await?;
		if $delay > 0 {
			delay($delay).await;
		}
	};
}

fn random_byte() -> u8 {
	so::init().expect("Sodiumoxide library failed to initialize.");
	randombytes::randombytes_uniform((u8::MAX as u32) + 1) as u8
}

async fn fake_loading(
	stream: &mut BufReader<TcpStream>,
	text: &str,
	dots: u8,
	delay: u64,
) -> Result<(), Box<dyn Error>>
{
	write_all_delay!(stream, delay, "{}", text);
	for _ in 0..dots {
		write_all_delay!(stream, delay, ".");
	}
	write_all_delay!(stream, NO_DELAY, "\n");

	Ok(())
}

async fn delay(secs: u64) { time::delay_for(Duration::new(secs, 0)).await; }

async fn internal_process(stream: TcpStream, config: &Config<'_>) -> Result<(), Box<dyn Error>> {
	let mut stream = BufReader::new(stream);
	let mut line = String::new();

	write_all_delay!(
		stream,
		STANDARD_DELAY,
		"Welcome to the flag retrieval service.\n"
	);
	write_all_delay!(stream, STANDARD_DELAY, "Robots may not use this service.\n");

	loop {
		let a = random_byte();
		let b = random_byte();
		let expected = (a as u16) + (b as u16);
		write_all_delay!(stream, 0, "What is {} + {} ?\n", a, b);
		line.clear();
		stream.read_line(&mut line).await?;
		fake_loading(&mut stream, "Checking answer", DOTS, STANDARD_DELAY).await?;

		if match line.trim_end().parse() {
			Ok(actual) if expected == actual => true,
			_ => false,
		} {
			write_all_delay!(stream, NO_DELAY, "Correct!\n");
			break;
		} else {
			write_all_delay!(stream, NO_DELAY, "Incorrect!\n");
		}
	}

	fake_loading(&mut stream, "Retrieving flag", DOTS, STANDARD_DELAY).await?;
	write_all_delay!(stream, NO_DELAY, "The flag is: {}\n", config.flag());

	Ok(())
}

pub async fn process(stream: TcpStream, config: &Config<'_>) {
	if let Err(_err) = internal_process(stream, config).await {
		#[cfg(debug_assertions)]
		eprintln!("{}", _err);
	}
}
