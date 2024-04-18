
django-admin startproject drfecommerce

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())


pip install python-dotenv