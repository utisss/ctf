#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use]
extern crate rocket;

use std::error::Error;

use rocket_contrib::serve::StaticFiles;
use so::crypto::auth::hmacsha256;
use sodiumoxide as so;

use challenge::api;
use to_jwt_or_not_to_jwt as challenge;
use to_jwt_or_not_to_jwt::api::{Alg, Flag, KeyStore, RedactedFlag, Users};

const FLAG_VAR: &str = "FLAG";
const REDACTED_FLAG_VAR: &str = "REDACTED_FLAG";
const PORT_VAR: &str = "PORT";

const DEFAULT_FLAG: Option<String> = None;
const DEFAULT_REDACTED_FLAG: Option<String> = None;
const DEFAULT_PORT: Option<u16> = Some(3000);

fn main() -> Result<(), Box<dyn Error>> {
    so::init().unwrap();

    let flag = to_jwt_or_not_to_jwt::env::get_var(FLAG_VAR, DEFAULT_FLAG)?;
    let redacted_flag =
        to_jwt_or_not_to_jwt::env::get_var(REDACTED_FLAG_VAR, DEFAULT_REDACTED_FLAG)?;
    let port = to_jwt_or_not_to_jwt::env::get_var(PORT_VAR, DEFAULT_PORT)?;

    let mut key_store = KeyStore::default();
    key_store.insert(Alg::HS256, hmacsha256::gen_key().0.to_vec());

    Err(rocket::custom(
        rocket::Config::build(rocket::config::Environment::Production)
            .port(port)
            .log_level(rocket::config::LoggingLevel::Off)
            .finalize()?,
    )
    .mount("/", StaticFiles::from("www").rank(30))
    .mount(
        "/api/v1",
        routes![
            api::authenticate,
            api::register,
            api::get_flag_admin,
            api::get_flag_user,
        ],
    )
    .manage(key_store)
    .manage(Flag::new(flag))
    .manage(RedactedFlag::new(redacted_flag))
    .manage(Users::default())
    .launch()
    .into())
}
