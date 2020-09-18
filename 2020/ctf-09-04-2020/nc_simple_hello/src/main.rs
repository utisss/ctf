use std::{
	error::Error,
	net::{IpAddr, Ipv6Addr, SocketAddr},
};

use lazy_static::lazy_static;
use sodiumoxide as so;
use tokio::net::TcpListener;

use nc_simple_hello::{Config, ConfigBuilder};

const FLAG_VAR: &str = "FLAG";
const LISTEN_PORT_VAR: &str = "LISTEN_PORT";
const LISTEN_ADDR_VAR: &str = "LISTEN_ADDR";
const DEFAULT_PORT: Option<u16> = Some(3000);
const DEFAULT_FLAG: Option<String> = None;

lazy_static! {
	static ref DEFAULT_LISTEN_ADDR: Option<IpAddr> = Some(IpAddr::V6(Ipv6Addr::from(0)));
}

lazy_static! {
	static ref FLAG: String = nc_simple_hello::env::get_var(FLAG_VAR, DEFAULT_FLAG).unwrap();
	static ref CONFIG: Config<'static> = ConfigBuilder::new().set_flag(&FLAG).finalize().unwrap();
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
	so::init().expect("Sodiumoxide library failed to initialize.");

	println!("{}", *CONFIG);

	let port = nc_simple_hello::env::get_var(LISTEN_PORT_VAR, DEFAULT_PORT)?;
	let addr = nc_simple_hello::env::get_var(LISTEN_ADDR_VAR, *DEFAULT_LISTEN_ADDR)?;

	let socket = SocketAddr::new(addr, port);
	let mut listener = TcpListener::bind(socket).await?;

	loop {
		match listener.accept().await {
			Ok((socket, _addr)) => {
				#[cfg(debug_assertions)]
				eprintln!("Connection from: {}", _addr);
				tokio::spawn(async {
					nc_simple_hello::process(socket, &CONFIG).await;
				});
			},
			Err(_err) => {
				#[cfg(debug_assertions)]
				eprintln!("{}", _err);
			},
		}
	}
}
