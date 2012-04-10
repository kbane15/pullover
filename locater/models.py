from django.db import models

class Intro(models.Model):
    words = models.TextField()
    def get_absolute_url(self):
        return "/locater/%i/" % self.id
    def __unicode__(self):
        return self.words

class Town(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=100)
    population = models.IntegerField()
    def get_absolute_url(self):
        return "/town/%i/" % self.id
    def __unicode__(self):
        return self.name
        return self.location
        return self.population


