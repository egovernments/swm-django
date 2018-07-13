from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class Request(models.Model):
    title = models.CharField('Title', max_length=30, default="Cleanliness")
    image = models.ImageField('Image', upload_to='images', default='images/request.png')
    source = models.CharField('Source', max_length=50)
    location = models.CharField('Location', max_length=100, blank=True, null=True)
    date = models.DateField('Date')
    time = models.TimeField('Time')
    approval = models.BooleanField(default=False)
    lat = models.FloatField(default=12.0)
    lng = models.FloatField(default=77.6)

class Point(models.Model):
    lat = models.FloatField(default=12.0)
    lng = models.FloatField(default=77.6)
    date = models.DateTimeField('Date', blank=True, null=True)
    on = models.BooleanField(default=False)
    source = models.CharField('Source', max_length=50, blank=True, null=True)


class RequestForm(ModelForm):
    # location = forms.CharField(max_length=128, help_text="champu")
    #location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Hostel 2, IIT Bombay, Powai, Mumbai - 400076', 'size' : 30}))
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date = forms.DateField(widget=SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Request
        fields = ('date', 'time', 'lat', 'lng')

class PointForm(ModelForm):
    # location = forms.CharField(max_length=128, help_text="champu")
    #location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Hostel 2, IIT Bombay, Powai, Mumbai - 400076', 'size' : 30}))
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date = forms.DateField(widget=SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Request
        fields = ('date', 'time')

class Requested(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    event = models.ForeignKey(Request, on_delete='CASCADE')

