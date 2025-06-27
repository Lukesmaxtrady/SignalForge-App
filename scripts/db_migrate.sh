#!/bin/bash
echo "Running DB migrations..."
cd ../src/db/migrations
for migration in *.py; do
  python "$migration"
done
echo "DB migrations complete."
