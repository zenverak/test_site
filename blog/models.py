# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):


    author = models.ForeignKey('auth.User', default=1)
    title = models.CharField(max_length=200, default='The Man')
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null=True)
    rating = models.IntegerField(default=0)

##    def __init__(self):
##        self.author = models.ForeignKey('auth.User')
##        self.title = models.CharField(max_length=200)
##        self.text = models.TextField()
##        self.created_date = models.DateTimeField(default=timezone.now)
##        self.published_date = models.DateTimeField(blank = True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
