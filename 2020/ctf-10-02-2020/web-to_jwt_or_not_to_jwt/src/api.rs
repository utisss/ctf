use std::collections::HashMap;
use std::sync::Mutex;

use rocket::http::{Cookie, Cookies, Status};
use rocket::request::{FromRequest, Outcome};
use rocket::{Request, State};
use rocket_contrib::json::Json;
use serde::{Deserialize, Serialize};
use so::crypto::pwhash::argon2id13;
use sodiumoxide as so;

use crate::jwt::JWTError;

use super::jwt;
pub use super::jwt::Alg;
pub use super::jwt::KeyStore;

const MEMLIMIT: argon2id13::MemLimit = argon2id13::MEMLIMIT_INTERACTIVE;
const OPSLIMIT: argon2id13::OpsLimit = argon2id13::OPSLIMIT_INTERACTIVE;

const TOKEN_COOKIE_NAME: &str = "token";

pub struct Users {
    users: Mutex<HashMap<String, StoredUser>>,
}

impl Default for Users {
    fn default() -> Self {
        Self {
            users: Mutex::new(HashMap::default()),
        }
    }
}

struct StoredUser {
    password: argon2id13::HashedPassword,
}

#[derive(Serialize, Deserialize)]
pub struct UnsafeUser {
    username: String,
    password: String,
}

#[derive(Serialize, Deserialize)]
pub struct VerifiedAccount {
    admin: bool,
    username: String,
}

pub struct AdminAccount();

impl<'a, 'r> AdminAccount {
    fn validate_token_cookie(
        request: &'a Request<'r>,
        key_store: &KeyStore,
        users: State<Users>,
    ) -> Result<Self, JWTError> {
        let token = request.cookies();
        let token = token
            .get(TOKEN_COOKIE_NAME)
            .map(|cookie| cookie.value())
            .ok_or(JWTError::InvalidToken)?;

        let account: VerifiedAccount = jwt::validate_jwt(token, key_store)?;

        let users = users
            .users
            .try_lock()
            .map_err(|_| JWTError::InternalError)?;
        if !users.contains_key(&account.username) {
            return Err(JWTError::InvalidToken);
        }
        drop(users);

        if account.admin {
            Ok(Self())
        } else {
            Err(JWTError::AuthorizationFail)
        }
    }
}

impl<'a, 'r> FromRequest<'a, 'r> for AdminAccount {
    type Error = JWTError;

    fn from_request(request: &'a Request<'r>) -> Outcome<Self, Self::Error> {
        let users = match request.guard::<State<Users>>() {
            Outcome::Success(s) => s,
            Outcome::Forward(_) => {
                return Outcome::Failure((Status::Unauthorized, JWTError::InternalError));
            }
            Outcome::Failure(_) => {
                return Outcome::Failure((Status::Unauthorized, JWTError::InternalError));
            }
        };

        request
            .guard::<State<KeyStore>>()
            .map_failure(|(_, _)| (Status::Unauthorized, JWTError::InvalidToken))
            .and_then(|key_store| {
                match AdminAccount::validate_token_cookie(request, &key_store, users) {
                    Result::Ok(res) => Outcome::Success(res),
                    Result::Err(err) if err == JWTError::AuthorizationFail => Outcome::Forward(()),
                    Result::Err(err) => Outcome::Failure((Status::Unauthorized, err)),
                }
            })
    }
}

pub struct RedactedFlag(String);

impl RedactedFlag {
    pub fn new(flag: String) -> Self {
        Self(flag)
    }
}

pub struct Flag(String);

impl Flag {
    pub fn new(flag: String) -> Self {
        Self(flag)
    }
}

#[post("/authenticate", format = "json", data = "<unsafe_user>")]
pub fn authenticate(
    mut cookies: Cookies,
    unsafe_user: Json<UnsafeUser>,
    key_store: State<KeyStore>,
    users: State<Users>,
) -> Status {
    let users = match users.users.try_lock() {
        Ok(guard) => guard,
        Err(_) => return Status::InternalServerError,
    };

    if let Some(user) = users.get(&*unsafe_user.username) {
        if argon2id13::pwhash_verify(&user.password, unsafe_user.password.as_bytes()) {
            let token = match jwt::create_jwt(
                &VerifiedAccount {
                    username: unsafe_user.username.clone(),
                    admin: false,
                },
                &key_store,
            ) {
                Ok(token) => token,
                Err(_) => return Status::InternalServerError,
            };

            cookies.add(Cookie::build(TOKEN_COOKIE_NAME, token).finish());

            return Status::Ok;
        }
    }

    Status::Unauthorized
}

#[post("/register", format = "json", data = "<unsafe_user>")]
pub fn register(
    mut cookies: Cookies,
    unsafe_user: Json<UnsafeUser>,
    key_store: State<KeyStore>,
    users: State<Users>,
) -> Status {
    let mut users = match users.users.try_lock() {
        Ok(guard) => guard,
        Err(_) => return Status::InternalServerError,
    };

    if unsafe_user.username.is_empty() || unsafe_user.password.is_empty() {
        return Status::BadRequest;
    }

    if !users.contains_key(&*unsafe_user.username) {
        let username = unsafe_user.username.clone();
        let password = match argon2id13::pwhash(unsafe_user.password.as_bytes(), OPSLIMIT, MEMLIMIT)
        {
            Ok(password) => password,
            Err(_) => return Status::InternalServerError,
        };

        users.insert(username.clone(), StoredUser { password });

        let token = match jwt::create_jwt(
            &VerifiedAccount {
                username,
                admin: false,
            },
            &key_store,
        ) {
            Ok(token) => token,
            Err(_) => return Status::InternalServerError,
        };

        cookies.add(Cookie::build(TOKEN_COOKIE_NAME, token).finish());

        return Status::Ok;
    }

    Status::AlreadyReported
}

#[get("/get_flag", rank = 1)]
pub fn get_flag_admin(_admin_account: AdminAccount, flag: State<Flag>) -> &str {
    &*flag.inner().0
}

#[get("/get_flag", rank = 2)]
pub fn get_flag_user(redacted_flag: State<RedactedFlag>) -> &str {
    &*redacted_flag.inner().0
}
