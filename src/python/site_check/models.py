from django.db import models

#class Coord(models.Model):
#    dt  = models.DateTimeField() #this is UTC ? (it's from fire-eagle)
#    name = models.CharField(max_length=256)
#    lat = models.FloatField()

class Site(models.Model):
    """
    a 'site' that needs checking.
    """
    name = models.CharField(max_length=256)
    added = models.DateTimeField()
