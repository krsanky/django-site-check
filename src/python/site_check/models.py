from django.db import models

class SiteCheck(models.Model):
    """
    a site/service that needs checking.
    """
    name = models.CharField(max_length=200)
    url = models.URLField()
    #port ???
    #protocol ssh ftp http ... etc. ???

    added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    def __unicode__(self):
        return str(self.name) + ": " + str(self.url)
