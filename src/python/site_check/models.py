from django.db import models
from django.contrib.auth.models import User

class CheckSite(models.Model):
    """
    a site/service that needs checking.
    """
    name = models.CharField(max_length=200)
    url = models.URLField()
    #port ???
    #protocol ssh ftp http ... etc. ???

    added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    notifees = models.ManyToManyField(User, null=True)

    def __unicode__(self):
        return str(self.name) + ": " + str(self.url)

class CheckLog(models.Model):
    """
    a write-once-only log for site status per-check
    """
    time = models.DateTimeField(auto_now_add=True)
    site = models.ForeignKey(CheckSite)
    status = models.CharField(max_length=4, choices=(('up', 'Up'),
                                                     ('down', 'Down'),
                                                     ))

