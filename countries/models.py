from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=50, blank=False, default='', verbose_name="Name")
    capital = models.CharField(max_length=100, blank=False, default='', verbose_name="Capital")

    class Meta:
        ordering = ('id',)