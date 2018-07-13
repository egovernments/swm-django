from django.db import models


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE,blank=True, null=True)
    subject = models.CharField(max_length=200)
    matter = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.subject
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
