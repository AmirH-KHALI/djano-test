from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)
    Religion = models.CharField(max_length=30)

class Student(models.Model):
    name = models.CharField(max_length=30)
    classType = models.CharField(max_length=1)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)