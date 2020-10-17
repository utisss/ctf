use std::{
	error::Error,
	net::{IpAddr, Ipv6Addr, SocketAddr},
};

use lazy_static::lazy_static;
use tokio::net::TcpListener;

use real_signature_algorithm as this_crate;
use this_crate::{Config, ConfigBuilder};

const FLAG_VAR: &str = "FLAG";
const LISTEN_PORT_VAR: &str = "LISTEN_PORT";
const LISTEN_ADDR_VAR: &str = "LISTEN_ADDR";
const READ_TIMEOUT_VAR: &str = "READ_TIMEOUT";
const BITS_VAR: &str = "BITS";
const SIGN_TRIES_VAR: &str = "SIGN_TRIES";
const VERIFY_TRIES_VAR: &str = "VERIFY_TRIES";

const DEFAULT_PORT: Option<u16> = Some(3000);
#[cfg(not(debug_assertions))]
const DEFAULT_FLAG: Option<&str> = None;
#[cfg(debug_assertions)]
const DEFAULT_FLAG: Option<&str> = Some("utflag{testing_only}");
#[cfg(not(debug_assertions))]
const DEFAULT_READ_TIMEOUT: Option<u64> = None;
#[cfg(debug_assertions)]
const DEFAULT_READ_TIMEOUT: Option<u64> = Some(120);
#[cfg(debug_assertions)]
const DEFAULT_BITS: Option<usize> = Some(512);
#[cfg(not(debug_assertions))]
const DEFAULT_BITS: Option<usize> = Some(4096);
const DEFAULT_SIGN_TRIES: Option<u8> = Some(2);
const DEFAULT_VERIFY_TRIES: Option<u8> = Some(1);

lazy_static! {
	static ref DEFAULT_LISTEN_ADDR: Option<IpAddr> = Some(IpAddr::V6(Ipv6Addr::from(0)));
}

lazy_static! {
	static ref FLAG: String = this_crate::env::get_var(
		FLAG_VAR,
		match DEFAULT_FLAG {
			Some(flag) => Some(flag.to_string()),
			None => None,
		}
	)
	.unwrap();
	static ref READ_TIMEOUT: u64 =
		this_crate::env::get_var(READ_TIMEOUT_VAR, DEFAULT_READ_TIMEOUT).unwrap();
	static ref BITS: usize = this_crate::env::get_var(BITS_VAR, DEFAULT_BITS).unwrap();
	static ref SIGN_TRIES: u8 =
		this_crate::env::get_var(SIGN_TRIES_VAR, DEFAULT_SIGN_TRIES).unwrap();
	static ref VERIFY_TRIES: u8 =
		this_crate::env::get_var(VERIFY_TRIES_VAR, DEFAULT_VERIFY_TRIES).unwrap();
	static ref CONFIG: Config<'static> = ConfigBuilder::new()
		.set_flag(&FLAG)
		.set_read_timeout(*READ_TIMEOUT)
		.set_bits(*BITS)
		.unwrap()
		.set_sign_tries(*SIGN_TRIES)
		.set_verify_tries(*VERIFY_TRIES)
		.finalize()
		.unwrap();
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
	println!("{}", *CONFIG);

	let port = this_crate::env::get_var(LISTEN_PORT_VAR, DEFAULT_PORT)?;
	let addr = this_crate::env::get_var(LISTEN_ADDR_VAR, *DEFAULT_LISTEN_ADDR)?;

	let socket = SocketAddr::new(addr, port);
	let mut listener = TcpListener::bind(socket).await?;

	loop {
		match listener.accept().await {
			Ok((socket, _addr)) => {
				#[cfg(debug_assertions)]
				eprintln!("Connection from: {}", _addr);
				tokio::spawn(async {
					this_crate::process(socket, &CONFIG).await;
				});
			},
			Err(_err) => {
				#[cfg(debug_assertions)]
				eprintln!("{}", _err);
			},
		}
	}
}
