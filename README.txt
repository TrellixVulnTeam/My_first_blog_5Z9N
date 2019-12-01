.\django_venv\Scripts\activate

If we are checking before deploy

python blog/manage.py check --deploy 

IN THE ROUTE blog/settings.py we need to disable DEBUG setting before deploy
and also ALLOWED_HOSTS = [*]

pip3 install gunicorn // I do not know why on the virtual env in linux server, maybe i will need to install it at local instance in the future also.
sudo apt-get install -y nginx // same as above

How to run server
env) ubuntu@ip-172-31-30-34:~/My_first_blog/blog$ gunicorn --bind 0.0.0.0:8000 blog.wsgi:applivation
