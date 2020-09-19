use std::{
	error::Error,
	net::{IpAddr, Ipv6Addr, SocketAddr},
};

use lazy_static::lazy_static;
use sodiumoxide as so;
use tokio::net::TcpListener;

use nc_complex_hello::{Config, ConfigBuilder};

const FLAG_VAR: &str = "FLAG";
const LISTEN_PORT_VAR: &str = "LISTEN_PORT";
const LISTEN_ADDR_VAR: &str = "LISTEN_ADDR";
const READ_TIMEOUT_VAR: &str = "READ_TIMEOUT";
const STANDARD_DELAY_VAR: &str = "STANDARD_DELAY";
const NO_DELAY_VAR: &str = "NO_DELAY";
const NUM_DOTS_VAR: &str = "NUM_DOTS";
const MINIMUM_QUESTIONS_VAR: &str = "MINIMUM_QUESTIONS";
const MAXIMUM_QUESTIONS_VAR: &str = "MAXIMUM_QUESTIONS";

const DEFAULT_PORT: Option<u16> = Some(3000);
const DEFAULT_FLAG: Option<String> = None;
const DEFAULT_READ_TIMEOUT: Option<u64> = None;
const DEFAULT_STANDARD_DELAY: Option<u64> = Some(0);
const DEFAULT_NO_DELAY: Option<u64> = Some(0);
const DEFAULT_NUM_DOTS: Option<u8> = Some(3);
const DEFAULT_MINIMUM_QUESTIONS: Option<u16> = None;
const DEFAULT_MAXIMUM_QUESTIONS: Option<u16> = None;

lazy_static! {
	static ref DEFAULT_LISTEN_ADDR: Option<IpAddr> = Some(IpAddr::V6(Ipv6Addr::from(0)));
}

lazy_static! {
	static ref FLAG: String = nc_complex_hello::env::get_var(FLAG_VAR, DEFAULT_FLAG).unwrap();
	static ref READ_TIMEOUT: u64 =
		nc_complex_hello::env::get_var(READ_TIMEOUT_VAR, DEFAULT_READ_TIMEOUT).unwrap();
	static ref STANDARD_DELAY: u64 =
		nc_complex_hello::env::get_var(STANDARD_DELAY_VAR, DEFAULT_STANDARD_DELAY).unwrap();
	static ref NO_DELAY: u64 =
		nc_complex_hello::env::get_var(NO_DELAY_VAR, DEFAULT_NO_DELAY).unwrap();
	static ref NUM_DOTS: u8 =
		nc_complex_hello::env::get_var(NUM_DOTS_VAR, DEFAULT_NUM_DOTS).unwrap();
	static ref MINIMUM_QUESTIONS: u16 =
		nc_complex_hello::env::get_var(MINIMUM_QUESTIONS_VAR, DEFAULT_MINIMUM_QUESTIONS).unwrap();
	static ref MAXIMUM_QUESTIONS: u16 =
		nc_complex_hello::env::get_var(MAXIMUM_QUESTIONS_VAR, DEFAULT_MAXIMUM_QUESTIONS).unwrap();
	static ref CONFIG: Config<'static> = ConfigBuilder::new()
		.set_flag(&FLAG)
		.set_read_timeout(*READ_TIMEOUT)
		.set_standard_delay(*STANDARD_DELAY)
		.set_no_delay(*NO_DELAY)
		.set_num_dots(*NUM_DOTS)
		.set_minimum_questions(*MINIMUM_QUESTIONS)
		.set_maximum_questions(*MAXIMUM_QUESTIONS)
		.finalize()
		.unwrap();
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
	so::init().expect("Sodiumoxide library failed to initialize.");

	println!("{}", *CONFIG);

	let port = nc_complex_hello::env::get_var(LISTEN_PORT_VAR, DEFAULT_PORT)?;
	let addr = nc_complex_hello::env::get_var(LISTEN_ADDR_VAR, *DEFAULT_LISTEN_ADDR)?;

	let socket = SocketAddr::new(addr, port);
	let mut listener = TcpListener::bind(socket).await?;

	loop {
		match listener.accept().await {
			Ok((socket, _addr)) => {
				#[cfg(debug_assertions)]
				eprintln!("Connection from: {}", _addr);
				tokio::spawn(async {
					nc_complex_hello::process(socket, &CONFIG).await;
				});
			},
			Err(_err) => {
				#[cfg(debug_assertions)]
				eprintln!("{}", _err);
			},
		}
	}
}
