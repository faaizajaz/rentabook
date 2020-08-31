web: gunicorn rentabook.wsgi:application --timeout 900
release: python manage.py makemigrations; python manage.py migrate --noinput
