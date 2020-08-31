web: gunicorn rentabook.wsgi:application --timeout 240
release: python manage.py makemigrations; python manage.py migrate --noinput
