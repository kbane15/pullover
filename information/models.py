import datetime
from locater.models import Town
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=75)
    about = models.TextField()
    photograph = models.ImageField(upload_to="static/foodphotos/")
    town = models.ForeignKey(Town)
    pub_date = models.DateTimeField('date published')
    def get_absolute_url(self):
        return "/food/%i/" % self.id
    def __unicode__(self):
        return self.name

class Entertainment(models.Model):
    name = models.CharField(max_length=75)
    about = models.TextField()
    photograph = models.ImageField(upload_to="static/entphotos/")
    town = models.ForeignKey(Town)
    pub_date = models.DateTimeField('date published')
    def get_absolute_url(self):
        return "/ent/%i/" % self.id
    def __unicode__(self):
        return self.name

class History(models.Model):
    about = models.TextField()
    town = models.ForeignKey(Town)
    pub_date = models.DateTimeField('date published')
    def get_absolute_url(self):
        return "/town/%i/" % self.id
    def __unicode__(self):
        return self.about
