from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)

class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)

class TV(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    screen_size = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
