#!/usr/bin/env bash

rm -rf ./backend/djangorest/apidoc/*
docker run -v $(PWD)/backend/djangorest:/app --name npm -i --rm -d node:10-slim bash -c "npm i -g apidoc && cd /app && apidoc -i ./apps -o ./apidoc"
#docker exec -it nginx bash -c "chown -R www-data. /var/www/html"
