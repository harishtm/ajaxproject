from django.db import models
from django.contrib import admin
# Create your models here.


class MyCountry(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    country = models.ForeignKey(MyCountry, blank=True, null=True)

    def __unicode__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    state = models.ForeignKey(State, blank=True, null=True)

    def __unicode__(self):
        return self.name



