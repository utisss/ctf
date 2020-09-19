FROM rust:latest as builder
ARG BIN_NAME

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
ARG LISTEN_PORT
ARG FLAG
ARG READ_TIMEOUT
ARG MINIMUM_QUESTIONS
ARG MAXIMUM_QUESTIONS
ARG APP=/usr/src/app

ENV LISTEN_PORT $LISTEN_PORT
ENV APP_USER $APP_USER
ENV FLAG $FLAG
ENV READ_TIMEOUT $READ_TIMEOUT
ENV MINIMUM_QUESTIONS $MINIMUM_QUESTIONS
ENV MAXIMUM_QUESTIONS $MAXIMUM_QUESTIONS

EXPOSE $LISTEN_PORT

RUN groupadd $APP_USER \
    && useradd -g $APP_USER $APP_USER \
    && mkdir -p ${APP}

COPY --from=builder /$BIN_NAME/target/release/$BIN_NAME ${APP}/$BIN_NAME

RUN chown -R $APP_USER:$APP_USER ${APP}

USER $APP_USER
WORKDIR ${APP}

CMD ["./nc_complex_hello"]
