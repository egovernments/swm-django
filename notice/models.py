from django.db import models
from django.contrib.auth.models import User
from events.models import Location


class Notice(models.Model):
    notice_source = models.CharField('Source', max_length=100)
    notice_title = models.CharField('Title', max_length=100)
    notice_description = models.TextField('Description', blank=True, null=True)
    notice_image = models.ImageField('Image', upload_to='images', blank=True, null=True, default='images/notice.jpg')
    publishing_location = models.ManyToManyField(Location)
    publishing_date = models.DateTimeField('Publishing Date', blank=False)

    def __str__(self):
        return self.notice_title
