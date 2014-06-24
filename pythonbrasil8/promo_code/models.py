# coding: utf-8

from django.db import models


class PromoCode(models.Model):
    code = models.CharField(max_length=10)
    email = models.EmailField(
        max_length=254, unique=True, blank=True, null=True,
    )
    sent = models.DateTimeField(null=True)  # TODO: Populate on save if email

    def __unicode__(self):
        return u'{email}: {code}'.format(code=self.code, email=self.email)
