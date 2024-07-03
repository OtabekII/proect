from django.db import models

# Create your models here.

class Myself(models.Model):
    full_name = models.CharField(max_length=255)
    profil = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    bio = models.TextField()
    img = models.ImageField()


class Servises(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()


class Portfolio(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)


class Blog(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    thame = models.CharField(max_length=255)
    message = models.TextField()


