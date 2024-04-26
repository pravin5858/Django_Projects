virtualenv env
env/scripts/activate
pip install django django-ninja django-extensions
pip freeze > requirments.txt
django-admin startproject devices_backend
pip install python-dotenv
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
