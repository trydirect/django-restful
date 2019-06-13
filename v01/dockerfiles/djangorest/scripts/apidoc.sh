#!/usr/bin/env bash

# IMPORTANT! Sometimes it takes up to 30 sec for apidoc to be generated

rm -rf $(pwd)/djangorest/src/backend/djangorest/static/apidoc/*
docker run -v $(pwd)/djangorest/src/backend/djangorest:/app --name npm -i --rm -d node:10-slim bash -c "npm i -g apidoc && cd /app && apidoc -i ./quickstart -o ./static/apidoc"
