use std::{
	error::Error,
	fmt::{self, Display, Formatter},
};

#[derive(Debug)]
pub enum ConfigBuilderError {
	MissingFlag,
	MissingReadTimeout,
	MissingBits,
	BadBits(usize),
	MissingSignTries,
	MissingVerifyTries,
}

impl Error for ConfigBuilderError {}

impl Display for ConfigBuilderError {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		match self {
			Self::MissingFlag => write!(f, "The flag is missing."),
			Self::MissingReadTimeout => write!(f, "The read_timout value is undefined."),
			Self::MissingBits => write!(f, "The bits value is undefined."),
			Self::BadBits(bits) => {
				write!(
					f,
					"The bits value must be 128, 256, 512, 1024, 2048, 4096, or 8192. Attempted to set it to {}.",
					bits,
				)
			},
			Self::MissingSignTries => write!(f, "The sign_tries value is undefined."),
			Self::MissingVerifyTries => write!(f, "The verify_tries value is undefined."),
		}
	}
}
