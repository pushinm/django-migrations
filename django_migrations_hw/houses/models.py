from django.db import models

# Create your models here.
class House(models.Model):
    city = models.CharField(verbose_name='Address', max_length=100)