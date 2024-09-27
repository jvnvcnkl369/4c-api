#!/bin/sh

# Run migrations
alembic upgrade head

# Run seeder
python seeder.py

# Create a file to indicate that initialization has been done
touch /app/.db_initialized