from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from events.models import Location
# Create your models here.

class Ward(models.Model):
	user = models.ForeignKey(User,on_delete='CASCADE')
	wards = models.ManyToManyField(Location)

def give_permission(sender, **kwargs):
	u=kwargs['instance']
	permission = Permission.objects.get(name='Can add event')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can add poll')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can add choice')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can change event')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can change poll')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can add notice')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can change notice')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can delete event')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can delete poll')
	u.user_permissions.add(permission)
	permission = Permission.objects.get(name='Can delete notice')
	u.user_permissions.add(permission)
	

post_save.connect(give_permission ,sender=User)
