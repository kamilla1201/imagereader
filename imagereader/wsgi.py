"""
WSGI config for imagereader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagereader.settings")
sys.path.append('/home/kamilla/imagereader')
sys.path.append('/home/kamilla/imagereader/imagereader')
sys.path.append('/home/kamilla/imagereader/imagereader/feed')

application = get_wsgi_application()
