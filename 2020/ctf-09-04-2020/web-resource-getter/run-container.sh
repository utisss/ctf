#!/bin/bash

export PORT=5006

export DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PROB_NAME=$(echo "${DIR##*/}" | cut -d- -f2-)
export PROB_TYPE=$(echo "${DIR##*/}" | cut -d- -f1)
export USER=$PROB_NAME

eval $(minikube docker-env)

kubectl delete deployment $PROB_NAME

docker build --build-arg USER=$USER --build-arg FLAG=$FLAG -t ${PROB_NAME}-frontend frontend
docker build --build-arg USER=$USER --build-arg FLAG=$FLAG -t ${PROB_NAME}-backend backend

envsubst "$(printf '${%s} ' $(env | sed 's/=.*//'))" < $DIR/kube.yaml > $DIR/kube.yaml.processed
kubectl apply -f $DIR/kube.yaml.processed

echo
echo "Access your problem at:"
minikube service ${PROB_NAME} --url
