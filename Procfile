web: gunicorn Grocery_store.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate