from PIL import Image
import requests
from io import BytesIO
import datetime, os
from django.conf import settings
from django import template
register = template.Library()
def date(value):
    mydate = datetime.datetime.strptime(value[:10], "%Y-%m-%d")
    return mydate.strftime("%d %b, %Y")
register.filter('date', date)