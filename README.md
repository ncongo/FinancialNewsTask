# FinancialNewsTask
Django based REST API service for financial news, using scraping service for collecting data from yahoo site with implemented scraper service scheduler using Celery.

Applying DB migrations:
python manage.py migrate

Starting Django:
python manage.py runserver

Starting worker:
celery -A FinancialNews worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

Starting celery beat:
celery -A FinancialNews beat -l info

Running tests:
python manage.py test
