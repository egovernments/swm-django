from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
from django.conf import settings
import datetime
from django.utils import timezone
import sys, time, os
from django.core.files import File
import urllib
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
# Create your models here.2
class Location(models.Model):
    location_name = models.CharField('Location', max_length=20)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_name = models.CharField('Category', max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"


class Event(models.Model):
    event_source = models.CharField('Source', max_length=100)
    event_category = models.ManyToManyField(Category)
    event_title = models.CharField('Title', max_length=100)
    event_description = models.TextField('Description', blank=True, null=True)
    event_image = models.ImageField('Image', upload_to='images', blank=True, null=True, default='images/events.jpg')
    event_location = models.CharField('Location', max_length=100)
    event_start_date = models.DateField('Start Date')
    event_end_date = models.DateField('End Date', blank=True, null=True)
    event_start_time = models.TimeField('Start Time', blank=True, null=True)
    event_end_time = models.TimeField('End Time', blank=True, null=True)
    publishing_location = models.ManyToManyField(Location)
    pub_date = models.DateTimeField('Publishing Date', blank=False, default=timezone.now)
    #eid = models.CharField('Source', max_length=100, blank=True, null=True)
    def __str__(self):
        return self.event_title

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.event_image.path):
            print('Yo')
            os.remove(self.event_image.path)
        print('Meow')
        super(Event, self).delete(*args, **kwargs)

class Attended(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

@receiver(models.signals.post_delete, sender=Event)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.event_image:
        if os.path.isfile(instance.event_image.path):
            if (instance.event_image.url[14:] != "events.jpg"):
                os.remove(instance.event_image.path)
                print(str(settings.MEDIA_ROOT) + "/cropped/" + str(instance.event_image.url)[14:])
                if os.path.isfile(str(settings.MEDIA_ROOT) + "/cropped/" + str(instance.event_image.url)[14:]):
                    os.remove(str(settings.MEDIA_ROOT) + "/cropped/" + str(instance.event_image.url)[14:])

# @receiver(post_save, sender=Event, dispatch_uid="update_image")
# def update_image(sender, instance, **kwargs):
#     original = Image.open(instance.event_image)
#     w,h = original.size
#     print(w)
#     print(h)
#     if (w - h) > 0:
#         left = (w - h) // 2
#         right = (w + h) // 2
#         top = 0
#         bottom = h
#     else:
#         left = 0
#         right = w
#         top = (h - w) // 2
#         bottom = (h + w) // 2
#     cropped_image = original.crop((left, top, right, bottom))
#     print(instance.event_image.url)
#     print(instance.event_image.url[14:])
#     cropped_image.save(settings.MEDIA_ROOT + instance.event_image.url.replace("images", "cropped")[6:], cropped_image.format)
#     print(str(settings.MEDIA_ROOT) + "/cropped" + str(instance.event_image.url)[14:])

def add_to_calendar(sender, **kwargs):
    print("hello")
    e = kwargs['instance']
    try:
      try:
        start_datetime = datetime.datetime.combine(e.event_start_date,e.event_start_time)
        end_datetime = datetime.datetime.combine(e.event_end_date,e.event_end_time)
      except:
        end_time = datetime.time(23,59)
        start_time = datetime.time(0,1)
        start_datetime = datetime.datetime.combine(e.event_start_date,start_time)
        end_datetime = datetime.datetime.combine(e.event_end_date,end_time)
    except:
      end_time = datetime.time(23,59)
      start_time = datetime.time(0,1)
      start_datetime = datetime.datetime.combine(e.event_start_date,start_time)
      end_datetime = datetime.datetime.combine(e.event_start_date,end_time)
      
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    event = {
      'summary': e.event_title,
      'location': e.event_location,
      'description': e.event_description,
      'start': {
        'dateTime': start_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        'timeZone': 'Asia/Calcutta',
      },
      'end': {
        'dateTime': end_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        'timeZone': 'Asia/Calcutta',
      },
      'recurrence': [
      ],
      'attendees': [
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

post_save.connect(add_to_calendar ,sender=Event)

# def del_from_calendar(sender, **kwargs):
#     print("hello")
#     e = kwargs['instance']
#     SCOPES = 'https://www.googleapis.com/auth/calendar'
#     store = file.Storage('credentials.json')
#     creds = store.get()
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
#         creds = tools.run_flow(flow, store)
#     service = build('calendar', 'v3', http=creds.authorize(Http()))
#     eid = e.eid
#     service.events().delete(calendarId='primary', eventId=eid).execute()


# post_delete.connect(add_to_calendar ,sender=Event)
