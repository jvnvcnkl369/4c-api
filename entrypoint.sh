#!/bin/sh

if [ ! -f /app/.db_initialized ]; then
    echo "Initializing database..."
    sh /app/init_db.sh
else
    echo "Database already initialized, skipping..."
fi

exec python server.py