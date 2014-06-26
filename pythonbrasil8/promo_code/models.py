# coding: utf-8

from django.db import models
from django.core.mail import send_mail
from django.utils.timezone import now
from django.conf import settings


class PromoCode(models.Model):
    code = models.CharField(max_length=10)
    email = models.EmailField(
        max_length=254, unique=True, blank=True, null=True,
    )
    sent = models.DateTimeField(null=True)

    def __unicode__(self):
        return u'{email}: {code}'.format(code=self.code, email=self.email)

    def send_email(self):
        subject = u'Get your PythonBrasil[10] promotional code'
        body = '''
        Hi,
        Congratulations, here is your discount code for being a PythonBrasil
        associated!

        Code: {}

        You can complete your registration going to <link>, and informing
        your discount code.

        Att.
            PythonBrasil[10] Team
        '''.format(self.code)
        sent = send_mail(
            subject=subject, message=body, recipient_list=['to@example.com'],
            from_email=settings.DEFAULT_FROM_EMAIL,
        )

        self.sent = now()
        self.save()

        return sent
