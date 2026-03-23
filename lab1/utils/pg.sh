#!/bin/bash

while IFS='=' read -r key value; do
    if [ "$key" = "DB_ADMIN" ]; then
        connection_string="$value"
    fi
done < .env

psql "$connection_string"
