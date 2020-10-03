FROM rust:latest as builder
ARG BIN_NAME

RUN apt-get update \
    && apt-get full-upgrade -y \
    && apt-get install -y libsodium-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
RUN rustup update nightly && rustup default nightly

RUN USER=root cargo new --bin $BIN_NAME
WORKDIR ./$BIN_NAME

COPY ./Cargo.toml ./Cargo.toml
RUN cargo build --release
RUN rm src/*.rs

ADD . ./

RUN rm ./target/release/deps/$BIN_NAME*
RUN cargo build --release


FROM debian:buster-slim
ARG BIN_NAME
ARG APP_USER
ARG PORT
ARG FLAG
ARG REDACTED_FLAG
ARG APP=/usr/src/app

ENV APP_USER $APP_USER
ENV PORT $PORT
ENV FLAG $FLAG
ENV REDACTED_FLAG $REDACTED_FLAG

EXPOSE $PORT

RUN groupadd $APP_USER \
    && useradd -g $APP_USER $APP_USER \
    && mkdir -p ${APP}

COPY --from=builder /$BIN_NAME/target/release/$BIN_NAME ${APP}/app
COPY --from=builder /$BIN_NAME/www/ ${APP}/www

RUN chown -R $APP_USER:$APP_USER ${APP}

USER $APP_USER
WORKDIR ${APP}

CMD ["./app"]
