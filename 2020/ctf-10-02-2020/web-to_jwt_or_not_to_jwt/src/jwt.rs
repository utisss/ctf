use std::collections::HashMap;
use std::convert::{TryFrom, TryInto};
use std::error::Error;
use std::fmt::{self, Display, Formatter};

use serde::{Deserialize, Serialize};
use so::crypto::auth::hmacsha256;
use sodiumoxide as so;

#[derive(Debug, PartialEq, Eq)]
pub enum JWTError {
    InvalidToken,
    AuthorizationFail,
    InternalError,
}

const BASE64_ENCODING: base64::Config = base64::URL_SAFE_NO_PAD;

impl Error for JWTError {}

impl Display for JWTError {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match self {
            Self::InvalidToken => write!(f, "Token is invalid."),
            Self::AuthorizationFail => write!(f, "Unauthorized."),
            Self::InternalError => write!(f, "Internal error."),
        }
    }
}

fn check_sig(alg: &Alg, pieces: &[&str; 3], key_store: &KeyStore) -> Result<(), JWTError> {
    let signature =
        base64::decode_config(pieces[2], BASE64_ENCODING).map_err(|_| JWTError::InvalidToken)?;

    match alg {
        Alg::None => {
            if !signature.is_empty() {
                Err(JWTError::InvalidToken)
            } else {
                Ok(())
            }
        }
        Alg::HS256 => {
            let key = key_store.key(&alg).ok_or(JWTError::InvalidToken)?;
            let key = hmacsha256::Key::from_slice(key).ok_or(JWTError::InvalidToken)?;

            let tag = hmacsha256::Tag::from_slice(&signature).ok_or(JWTError::InvalidToken)?;

            if !hmacsha256::verify(
                &tag,
                (pieces[0].to_owned() + "." + pieces[1]).as_bytes(),
                &key,
            ) {
                Err(JWTError::InvalidToken)
            } else {
                Ok(())
            }
        }
    }
}

fn sign_token(alg: &Alg, data: &str, key_store: &KeyStore) -> Result<String, JWTError> {
    Ok(match alg {
        Alg::None => String::new(),
        Alg::HS256 => {
            let key = key_store.key(&alg).ok_or(JWTError::InternalError)?;
            let key = hmacsha256::Key::from_slice(key).ok_or(JWTError::InternalError)?;

            let tag = hmacsha256::authenticate(data.as_bytes(), &key);
            base64::encode_config(tag.0, BASE64_ENCODING)
        }
    })
}

pub fn validate_jwt<'a, T>(token: &'a str, key_store: &KeyStore) -> Result<T, JWTError>
where
    T: for<'de> Deserialize<'de>,
{
    let pieces: Vec<_> = token.split('.').collect();
    let pieces: Box<[&str; 3]> = pieces
        .into_boxed_slice()
        .try_into()
        .map_err(|_| JWTError::InvalidToken)?;
    let pieces = *pieces;

    let header = Header::from_encoded(pieces[0])?;
    let alg = Alg::try_from(&*header.alg)?;

    check_sig(&alg, &pieces, key_store)?;

    let payload_str: Vec<u8> = base64::decode(pieces[1])
        .map_err(|_| JWTError::InvalidToken)?
        .iter()
        .copied()
        .collect();

    let payload: T = serde_json::from_reader(&*payload_str).map_err(|_| JWTError::InvalidToken)?;

    Ok(payload)
}

pub fn create_jwt<T>(payload: &T, key_store: &KeyStore) -> Result<String, JWTError>
where
    T: Serialize,
{
    let payload = serde_json::to_string(payload).map_err(|_| JWTError::InternalError)?;
    let payload = base64::encode_config(payload, BASE64_ENCODING);

    let header = Header::default();
    let alg = Alg::try_from(&*header.alg).unwrap();
    let header = serde_json::to_string(&header).map_err(|_| JWTError::InternalError)?;
    let header = base64::encode_config(header, BASE64_ENCODING);

    let data = header + "." + &*payload;
    let signature = sign_token(&alg, &*data, key_store)?;
    Ok(data + "." + &*signature)
}

pub struct KeyStore {
    keys: HashMap<Alg, Vec<u8>>,
}

impl Default for KeyStore {
    fn default() -> Self {
        Self {
            keys: HashMap::new(),
        }
    }
}

impl KeyStore {
    pub fn key(&self, alg: &Alg) -> Option<&[u8]> {
        Some(&self.keys.get(alg)?)
    }

    pub fn insert(&mut self, alg: Alg, key: Vec<u8>) {
        self.keys.insert(alg, key);
    }
}

#[derive(Hash, PartialEq, Eq)]
pub enum Alg {
    None,
    HS256,
}

impl Display for Alg {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match self {
            Self::None => write!(f, "none"),
            Self::HS256 => write!(f, "HS256"),
        }
    }
}

impl TryFrom<&str> for Alg {
    type Error = JWTError;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        if value == Self::None.to_string() {
            Ok(Self::None)
        } else if value == Self::HS256.to_string() {
            Ok(Self::HS256)
        } else {
            Err(Self::Error::InvalidToken)
        }
    }
}

#[derive(Serialize, Deserialize)]
struct Header {
    alg: String,
}

impl Default for Header {
    fn default() -> Self {
        Self {
            alg: Alg::HS256.to_string(),
        }
    }
}

impl Header {
    pub fn from_encoded(header: &str) -> Result<Self, JWTError> {
        let header: String = base64::decode(header)
            .map_err(|_| JWTError::InvalidToken)?
            .iter()
            .map(|&val| val as char)
            .collect();

        let header = &header;

        let header: Header = serde_json::from_str(header).map_err(|_| JWTError::InvalidToken)?;

        Ok(header)
    }
}
