# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date =models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publshed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    