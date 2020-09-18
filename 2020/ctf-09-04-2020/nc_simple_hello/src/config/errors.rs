use std::{
	error::Error,
	fmt::{self, Display, Formatter},
};

#[derive(Debug)]
pub enum ConfigBuilderError {
	MissingFlag,
}

impl Error for ConfigBuilderError {}

impl Display for ConfigBuilderError {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		match self {
			Self::MissingFlag => write!(f, "The flag is missing."),
		}
	}
}
