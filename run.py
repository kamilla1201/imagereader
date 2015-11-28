#!/usr/bin/python  
# -*- coding: UTF-8 -*-

import os  
import sys
import django

sys.path.append('/home/kamilla/imagereader/')   
os.environ['DJANGO_SETTINGS_MODULE'] = 'imagereader.settings'

from django.contrib.auth.models import User  
from imagereader.feed.models import *
from imagereader import views
def update_img():  
    django.setup()
    sources = Source.objects.all()
    for source in sources:
    	views.add_images(source)


if __name__ == "__main__":  
    update_img()
