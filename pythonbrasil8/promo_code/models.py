# coding: utf-8

from django.db import models
from django.core.mail import send_mail
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from django.template.loader import get_template
from django.template import Context


class PromoCode(models.Model):
    code = models.CharField(max_length=10)
    email = models.EmailField(
        max_length=254, unique=True, blank=True, null=True,
    )
    sent = models.DateTimeField(null=True)

    def __unicode__(self):
        return u'{email}: {code}'.format(code=self.code, email=self.email)

    def send_email(self):
        ctx = Context({'code': self.code})
        body = get_template('promo_code/email_promo_code.txt').render(ctx)
        subject = _(u'Get your PythonBrasil[10] promotional code')

        sent = send_mail(
            subject=subject, message=body, recipient_list=[self.email],
            from_email=settings.DEFAULT_FROM_EMAIL,
        )

        self.sent = now()
        self.save()

        return sent
