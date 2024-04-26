virtualenv env


pip install django

django-admin startproject drfecommerce

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())


pip install python-dotenv

pip install djangorestframework

pip install pytest

pip install pytest-django

pip install django-mptt
 
pip install drf-spectacular

python manage.py spectacular --file schema.py