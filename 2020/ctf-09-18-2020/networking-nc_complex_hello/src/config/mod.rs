use std::fmt::{self, Display, Formatter};

use crate::config::errors::ConfigBuilderError;

pub mod errors;

pub struct ConfigBuilder<'a> {
	flag: Option<&'a str>,
	read_timeout: Option<u64>,
	standard_delay: Option<u64>,
	no_delay: Option<u64>,
	num_dots: Option<u8>,
	minimum_questions: Option<u16>,
	maximum_questions: Option<u16>,
}

impl Default for ConfigBuilder<'_> {
	fn default() -> Self {
		Self {
			flag: None,
			read_timeout: None,
			standard_delay: None,
			no_delay: None,
			num_dots: None,
			minimum_questions: None,
			maximum_questions: None,
		}
	}
}

impl<'a> ConfigBuilder<'a> {
	pub fn new() -> Self { Self::default() }

	pub fn set_flag(mut self, flag: &'a str) -> Self {
		self.flag = Some(flag);

		self
	}

	pub fn set_read_timeout(mut self, read_timeout: u64) -> Self {
		self.read_timeout = Some(read_timeout);

		self
	}

	pub fn set_standard_delay(mut self, standard_delay: u64) -> Self {
		self.standard_delay = Some(standard_delay);

		self
	}

	pub fn set_no_delay(mut self, no_delay: u64) -> Self {
		self.no_delay = Some(no_delay);

		self
	}

	pub fn set_num_dots(mut self, num_dots: u8) -> Self {
		self.num_dots = Some(num_dots);

		self
	}

	pub fn set_minimum_questions(mut self, minimum_questions: u16) -> Self {
		self.minimum_questions = Some(minimum_questions);

		self
	}

	pub fn set_maximum_questions(mut self, maximum_questions: u16) -> Self {
		self.maximum_questions = Some(maximum_questions);

		self
	}

	pub fn finalize(self) -> Result<Config<'a>, ConfigBuilderError> {
		let flag = self.flag.ok_or(ConfigBuilderError::MissingFlag)?;
		let read_timeout = self
			.read_timeout
			.ok_or(ConfigBuilderError::MissingReadTimeout)?;
		let standard_delay = self
			.standard_delay
			.ok_or(ConfigBuilderError::MissingStandardDelay)?;
		let no_delay = self.no_delay.ok_or(ConfigBuilderError::MissingNoDelay)?;
		let num_dots = self.num_dots.ok_or(ConfigBuilderError::MissingNumDots)?;
		let minimum_questions = self
			.minimum_questions
			.ok_or(ConfigBuilderError::MissingMinimumQuestions)?;
		let maximum_questions = self
			.maximum_questions
			.ok_or(ConfigBuilderError::MissingMaximumQuestions)?;

		Ok(Config {
			flag,
			read_timeout,
			standard_delay,
			no_delay,
			num_dots,
			minimum_questions,
			maximum_questions,
		})
	}
}

pub struct Config<'a> {
	flag: &'a str,
	read_timeout: u64,
	standard_delay: u64,
	no_delay: u64,
	num_dots: u8,
	minimum_questions: u16,
	maximum_questions: u16,
}

impl Config<'_> {
	pub fn flag(&self) -> &str { &self.flag }

	pub fn read_timeout(&self) -> u64 { self.read_timeout }

	pub fn standard_delay(&self) -> u64 { self.standard_delay }

	pub fn no_delay(&self) -> u64 { self.no_delay }

	pub fn num_dots(&self) -> u8 { self.num_dots }

	pub fn minimum_questions(&self) -> u16 { self.minimum_questions }

	pub fn maxmimum_questions(&self) -> u16 { self.maximum_questions }
}

impl Display for Config<'_> {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		write!(
			f,
			"Configuration:\n\
            ==> Flag:              {}\n\
            ==> Read Timeout:      {}\n\
            ==> Standard Delay:    {}\n\
            ==> No Delay:          {}\n\
            ==> Num Dots:          {}\n\
            ==> Minimum Questions: {}\n\
            ==> Maximum Questions: {}\n\
            ",
			self.flag,
			self.read_timeout,
			self.standard_delay,
			self.no_delay,
			self.num_dots,
			self.minimum_questions,
			self.maximum_questions
		)
	}
}
