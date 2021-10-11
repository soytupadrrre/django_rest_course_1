from django.db import models

# Create your models here.

class Countries(models.Model):
    """
    Country model

    .. note::
        name: Varchar(50), blank=False, Default=''
        capital: Varchar(50), blank=False, Default=''

    :param models: super class Django Models
    :type models: class
    """
    name = models.CharField(max_length=50, blank=False, default='', verbose_name="Name")
    capital = models.CharField(max_length=100, blank=False, default='', verbose_name="Capital")

    class Meta:
        """
        Subclass for manage the model
        """
        ordering = ('id',)