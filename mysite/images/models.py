from django.db import models
import datetime
# Create your models here.

class ImagesClass(models.Model):
    user = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=16, null=True)
    location = models.CharField(max_length=256, null=True)
    create_time = models.DateTimeField(default=datetime.datetime.now())
    image = models.TextField()
    lable = models.TextField()
