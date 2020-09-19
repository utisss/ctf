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

async fn read_line<T>(
	stream: &mut T,
	buf: &mut String,
	config: &Config<'_>,
) -> Result<usize, tokio::io::Error>
where
	T: AsyncBufReadExt + Unpin,
{
	Ok(time::timeout(
		Duration::new(config.read_timeout(), 0),
		stream.read_line(buf),
	)
	.await??)
}

async fn fake_loading<T>(
	stream: &mut T,
	text: &str,
	dots: u8,
	delay: u64,
	config: &Config<'_>,
) -> Result<(), Box<dyn Error>>
where
	T: AsyncWriteExt + Unpin,
{
	write_all_delay!(stream, delay, "{}", text);
	for _ in 0..dots {
		write_all_delay!(stream, delay, ".");
	}
	write_all_delay!(stream, config.no_delay(), "\n");

	Ok(())
}

async fn delay(secs: u64) { time::delay_for(Duration::new(secs, 0)).await; }

async fn internal_process(stream: TcpStream, config: &Config<'_>) -> Result<(), Box<dyn Error>> {
	let mut stream = BufReader::new(stream);
	let mut line = String::new();

	write_all_delay!(
		stream,
		config.standard_delay(),
		"Welcome to the flag retrieval service.\n"
	);
	write_all_delay!(
		stream,
		config.standard_delay(),
		"Robots may not use this service.\n"
	);

	let max_rand_questions = config.maxmimum_questions() - config.minimum_questions() + 1;
	let rand_questions = randombytes::randombytes_uniform(max_rand_questions as u32) as u16;
	let questions = config.minimum_questions() + rand_questions;

	for _ in 0..questions {
		loop {
			let a = random_byte();
			let b = random_byte();
			let expected = (a as u16) + (b as u16);
			write_all_delay!(stream, 0, "What is {} + {} ?\n", a, b);
			line.clear();
			read_line(&mut stream, &mut line, config).await?;
			fake_loading(
				&mut stream,
				"Checking answer",
				config.num_dots(),
				config.standard_delay(),
				config,
			)
			.await?;

			if match line.trim_end().parse() {
				Ok(actual) if expected == actual => true,
				_ => false,
			} {
				write_all_delay!(stream, config.no_delay(), "Correct!\n");
				break;
			} else {
				write_all_delay!(stream, config.no_delay(), "Incorrect!\n");
				stream.shutdown().await?;
			}
		}
	}

	fake_loading(
		&mut stream,
		"Retrieving flag",
		config.num_dots(),
		config.standard_delay(),
		config,
	)
	.await?;
	write_all_delay!(
		stream,
		config.no_delay(),
		"The flag is: {}\n",
		config.flag()
	);

	Ok(())
}

pub async fn process(stream: TcpStream, config: &Config<'_>) {
	if let Err(_err) = internal_process(stream, config).await {
		#[cfg(debug_assertions)]
		eprintln!("{}", _err);
	}
}
