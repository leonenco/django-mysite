from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class Categories(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title

    #Rewrite plural name of the class in admin panel
    class Meta:
        verbose_name_plural = "categories"


class Projects(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    customer = models.CharField(default="", max_length=200)
    value = models.IntegerField(default=0)
    date_created = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def created_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

    # Rewrite plural name of the class in admin panel
    class Meta:
        verbose_name_plural = "projects"