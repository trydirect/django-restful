#!/bin/bash
#/docker-entrypoint-initdb.d/init-user-db.sh:

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER flask;
    CREATE DATABASE flask;
    GRANT ALL PRIVILEGES ON DATABASE flask TO flask;
EOSQL