from django.db import models
from datetime import datetime

# Create your models here.
#model for photos

class tsc_stores(models.Model):
    store_name = models.CharField(max_length=100)
    store_code = models.CharField(max_length=4)
    store_createdate = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.store_name


class photo_upload(models.Model):
    store_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/")
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.store_name

class brand_names(models.Model):
    brand_Name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.brand_Name


# modelforms

class Person_details(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)
    age = models.CharField(max_length=2)

    def __str__(self):
        return self.name

