#!/usr/bin/env bash

rm -rf ./backend/djangorest/apidoc/*
docker run -v $(pwd)/backend/djangorest:/app --name npm -i --rm -d node:10-slim bash -c "npm i -g apidoc && cd /app && apidoc -i ./quickstart -o ./apidoc"
#docker exec -it nginx bash -c "chown -R www-data. /var/www/html"
