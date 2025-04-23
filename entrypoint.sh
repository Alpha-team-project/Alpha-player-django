#!/bin/sh

if [ "$DB_USER" = "postgres" ]; then
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
fi

python3 manage.py migrate
python3 manage.py tailwind install --no-input
python3 manage.py tailwind build --no-input
# python manage.py collectstatic --no-input

exec "$@"