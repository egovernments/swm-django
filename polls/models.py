from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User
from events.models import Location


class Choice(models.Model):
    choice_name = models.CharField('Choice', max_length=30)
    choice_poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    choice_count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_name


class Poll(models.Model):
    poll_source = models.CharField('Source', max_length=100)
    poll_title = models.CharField('Title', max_length=100)
    poll_description = models.TextField('Description', blank=True, null=True)
    poll_image = models.ImageField('Image', upload_to='images', blank=True, null=True, default='images/poll.jpg')
    poll_deadline = models.DateTimeField('Deadline', blank=False)
    publishing_location = models.ManyToManyField(Location)
    pub_date = models.DateTimeField('Publishing Date', blank=False)

    def __str__(self):
        return self.poll_title


class Voted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + "->" + str(self.poll) + "->" + str(self.choice)
