import urllib2

from site_check.models import CheckSite
from site_check.models import CheckLog
from site_check.email import site_down_email

def check_sites():
    """
    get a list of all sites to check (active ones)
    and ping em or whatever.
    """
    sites = CheckSite.objects.filter(active=True)
    for s in sites:
        log = CheckLog(site=s)
        if not read_url(s.url):
            #print s.name + ' down'
            log.status = 'down'
            site_down_email(s)
        else:
            log.status = 'up'
            #print s.name + ' up'
        log.save()

def read_url(url):
    try:
        data = urllib2.urlopen(url).read()
        #print('Fetched %s from %s' % (len(data), url))
        return True
    except urllib2.URLError:
        return False




