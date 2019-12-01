.\django_venv\Scripts\activate

If we are checking before deploy

python blog/manage.py check --deploy 

IN THE ROUTE blog/settings.py we need to disable DEBUG setting before deploy
and also ALLOWED_HOSTS = [*]