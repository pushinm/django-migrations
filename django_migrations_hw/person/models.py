from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)
    age = models.IntegerField(verbose_name='age', default=18)