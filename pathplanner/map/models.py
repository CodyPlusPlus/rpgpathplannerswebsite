from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Maps(models.Model):
    mID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50)
    filepath = models.TextField(null=False)
    rows = models.IntegerField(null=False)
    cols = models.IntegerField(null=False)
    scale = models.FloatField()
    

class Paths(models.Model):
    pID = models.AutoField(primary_key=True)
    mID = models.ForeignKey(Maps, models.CASCADE)
    

class Waypoints(models.Model):
    wID = models.AutoField(primary_key=True)
    pID = models.ForeignKey(Paths, models.CASCADE)
    pxRow =  models.IntegerField(null=False)
    pxCol = models.IntegerField(null=False)


