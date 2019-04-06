#!/usr/bin/python3

import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 'j^-lqb85ohljo8ek%_kfc#+9+-!i%jtfh+j2x$(a6z%ltb)+&#')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
    TEMPLATE_BACKEND=(
        'django.template.backends.django.DjangoTemplates',
        ),
    SITE_PAGES_DIRECTORY=os.path.join(os.path.join(BASE_DIR, 'sitebuilder'), 'pages'),
    APP_DIRS=True,
)

print(dir(settings.configure))

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
