use std::fmt::{self, Display, Formatter};

use crate::config::errors::ConfigBuilderError;

pub mod errors;

pub struct ConfigBuilder<'a> {
	flag: Option<&'a str>,
	read_timeout: Option<u64>,
	bits: Option<usize>,
	sign_tries: Option<u8>,
	verify_tries: Option<u8>,
}

impl Default for ConfigBuilder<'_> {
	fn default() -> Self {
		Self {
			flag: None,
			read_timeout: None,
			bits: None,
			sign_tries: None,
			verify_tries: None,
		}
	}
}

impl<'a> ConfigBuilder<'a> {
	pub fn new() -> Self { Self::default() }

	pub fn set_flag(&mut self, flag: &'a str) -> &mut Self {
		self.flag = Some(flag);

		self
	}

	pub fn set_read_timeout(&mut self, read_timeout: u64) -> &mut Self {
		self.read_timeout = Some(read_timeout);

		self
	}

	pub fn set_bits(&mut self, bits: usize) -> Result<&mut Self, ConfigBuilderError> {
		if bits % 128 == 0 && bits >= 128 && bits <= 8192 {
			self.bits = Some(bits);
			Ok(self)
		} else {
			Err(ConfigBuilderError::BadBits(bits))
		}
	}

	pub fn set_sign_tries(&mut self, sign_tries: u8) -> &mut Self {
		self.sign_tries = Some(sign_tries);

		self
	}

	pub fn set_verify_tries(&mut self, verify_tries: u8) -> &mut Self {
		self.verify_tries = Some(verify_tries);

		self
	}

	pub fn finalize(&self) -> Result<Config<'a>, ConfigBuilderError> {
		let flag = self.flag.ok_or(ConfigBuilderError::MissingFlag)?;
		let read_timeout = self
			.read_timeout
			.ok_or(ConfigBuilderError::MissingReadTimeout)?;
		let bits = self.bits.ok_or(ConfigBuilderError::MissingBits)?;
		let sign_tries = self
			.sign_tries
			.ok_or(ConfigBuilderError::MissingSignTries)?;
		let verify_tries = self
			.verify_tries
			.ok_or(ConfigBuilderError::MissingVerifyTries)?;

		Ok(Config {
			flag,
			read_timeout,
			bits,
			sign_tries,
			verify_tries,
		})
	}
}

pub struct Config<'a> {
	flag: &'a str,
	read_timeout: u64,
	bits: usize,
	sign_tries: u8,
	verify_tries: u8,
}

impl Config<'_> {
	pub fn flag(&self) -> &str { &self.flag }

	pub fn read_timeout(&self) -> u64 { self.read_timeout }

	pub fn bits(&self) -> usize { self.bits }

	pub fn sign_tries(&self) -> u8 { self.sign_tries }

	pub fn verify_tries(&self) -> u8 { self.verify_tries }
}

impl Display for Config<'_> {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		write!(
			f,
			"Configuration:\n\
            ==> Flag:            {}\n\
            ==> Read Timeout:    {}\n\
            ==> Prime Bits:      {}\n\
            ==> Sign Tries:      {}\n\
            ==> Verify Tries:    {}\n\
            ",
			self.flag, self.read_timeout, self.bits, self.sign_tries, self.verify_tries,
		)
	}
}
