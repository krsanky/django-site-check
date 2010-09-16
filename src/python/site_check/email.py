from django.core.mail import send_mail
from django.core.mail import EmailMessage, SMTPConnection
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import loader, Context

def site_down_email(site):
    """
    basic email sending test
    """
    #get the sites users:
    #emails = [u['email'] for u in site.notifees.filter(is_active=True,email__isnull=False)]
    emails = site.notifees.filter(is_active=True,email__isnull=False).values_list('email', flat=True)

    data = {'site': site}
    t = loader.get_template("email/test_email.txt")
    #to = 'wise@lupulin.net'
    subject = '[site check] ' + str(site.url)
    body = t.render(Context(data))

    send_mail(subject,
              body,
              'from@example.com', #w/google this is forced i think
              emails,
              fail_silently=False)


