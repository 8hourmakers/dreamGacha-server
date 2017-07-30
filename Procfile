web: newrelic-admin run-program gunicorn --pythonpath="$PWD/dreamgacha" wsgi:application
worker: python dreamgacha/manage.py rqworker default