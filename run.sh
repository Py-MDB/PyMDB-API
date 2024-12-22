#!/usr/bin/env bash

docker build -t pymdb-api .
docker run --env-file .env -p 5000:5000 --network pymdb_network pymdb-api
