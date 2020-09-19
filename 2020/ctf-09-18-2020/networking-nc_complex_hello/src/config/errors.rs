use std::{
	error::Error,
	fmt::{self, Display, Formatter},
};

#[derive(Debug)]
pub enum ConfigBuilderError {
	MissingFlag,
	MissingReadTimeout,
	MissingStandardDelay,
	MissingNoDelay,
	MissingNumDots,
	MissingMinimumQuestions,
	MissingMaximumQuestions,
}

impl Error for ConfigBuilderError {}

impl Display for ConfigBuilderError {
	fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
		match self {
			Self::MissingFlag => write!(f, "The flag is missing."),
			Self::MissingReadTimeout => write!(f, "The read_timout value is undefined."),
			Self::MissingStandardDelay => write!(f, "The standard_delay value is undefined."),
			Self::MissingNoDelay => write!(f, "The no_delay value is undefined."),
			Self::MissingNumDots => write!(f, "The num_dots value is undefined."),
			Self::MissingMinimumQuestions => write!(f, "The minimum_questions value is undefined."),
			Self::MissingMaximumQuestions => write!(f, "The maximum_questions value is undefined."),
		}
	}
}
