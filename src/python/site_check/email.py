from django.core.mail import send_mail

def test_email():
    """
    basic email sending test
    """
    to = 'wise@lupulin.net'
    send_mail('Subject here',
              'Here is the message.',
              'from@example.com', #w/google this is forced i think
              [to], fail_silently=False)
