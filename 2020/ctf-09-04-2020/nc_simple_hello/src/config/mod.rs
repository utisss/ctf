use std::fmt::{self, Display, Formatter};

use crate::config::errors::ConfigBuilderError;

pub mod errors;

pub struct ConfigBuilder<'a> {
	flag: Option<&'a str>,
}

impl<'a> Default for ConfigBuilder<'a> {
	fn default() -> ConfigBuilder<'a> { ConfigBuilder { flag: None } }
}

impl<'a> ConfigBuilder<'a> {
	pub fn new() -> ConfigBuilder<'a> { ConfigBuilder { flag: None } }

	pub fn set_flag(mut self, flag: &'a str) -> Self {
		self.flag = Some(flag);

		self
	}

	pub fn finalize(self) -> Result<Config<'a>, ConfigBuilderError> {
		let flag = self.flag.ok_or(ConfigBuilderError::MissingFlag)?;

		Ok(Config { flag })
	}
}

pub struct Config<'a> {
	flag: &'a str,
}

impl Config<'_> {
	pub fn flag(&self) -> &str { &self.flag }
}

impl Display for Config<'_> {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		write!(
			f,
			"Configuration:\n\
            ==> Flag: {}\
            ",
			self.flag
		)
	}
}
