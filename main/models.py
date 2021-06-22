from django.db import models

# Create your models here.
class EmailList(models.Model):
    email = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.email

class Application(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200)
    package = models.CharField(max_length=200)

    def __str__(self):
        return self.email