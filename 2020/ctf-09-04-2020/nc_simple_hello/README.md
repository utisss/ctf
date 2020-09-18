# Simple Netcat Hello
This project serves as a template and reference for creating a simple TCP server in Rust.
The server handles connections concurrently using the [tokio](https://github.com/tokio-rs/tokio) crate.

## Configuration
The `docker-compose.yml` file contains the configuration for starting and running the app.
<br><br>
Run: `docker-compose up` <br>
Run headless: `docker-compose up -d`

## Testing and CI
Yaml files for using Restyled, Codecov, and TravisCI are present.<br>
Code is formatted by running `cargo +nightly fmt`<br>
Formatting rules are set in `rustfmt.toml`
<br><br>
Tests can be run with `cargo test`<br>
There are no tests in this project as of now.<br>
The nightly version of Rust needs to be available for generating a coverage report and formatting code.
To generate a coverage report with grcov, run the following script:
```bash
#!/bin/bash

set -e

export CARGO_INCREMENTAL=0
export RUSTFLAGS="-Zprofile -Ccodegen-units=1 -Copt-level=0 -Clink-dead-code -Coverflow-checks=off -Zpanic_abort_tests -Cpanic=abort"
export RUSTDOCFLAGS="-Cpanic=abort"

cargo +nightly build --verbose $CARGO_OPTIONS
cargo +nightly test --verbose $CARGO_OPTIONS

/usr/bin/grcov ./target/debug/ -s . -t html --llvm --branch --ignore-not-existing -o ./target/debug/coverage/
```
The script assumes the grcov binary is at `/usr/bin/grcov`
