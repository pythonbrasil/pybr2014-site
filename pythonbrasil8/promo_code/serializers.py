# coding: utf-8

import requests

from django.utils.translation import ugettext as _

from rest_framework import serializers

from pythonbrasil8.promo_code.models import PromoCode


class PromoCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def is_associated(self, email):
        # TODO: CPF
        try:
            response = requests.get(
                'http://associados.python.org.br/members/status/',
                params={'email': email},
            )
        except requests.exceptions.ConnectionError:
            raise serializers.ValidationError(
                _(u'Problem connecting with third party service'),
            )
        else:
            return response.json()['status'] == 'active'

    def validate_email(self, attrs, source):
        email = attrs[source]
        if not self.is_associated(email):
            raise serializers.ValidationError(
                _(u'E-mail is not valid associated email'),
            )

        return attrs

    def save(self):
        try:
            # TODO: Lock
            pc = PromoCode.objects.get(email=self.data['email'])
        except PromoCode.DoesNotExist:
            pc = PromoCode.objects.filter(email__isnull=True)[0]
            pc.email = self.data['email']
            pc.save()

        return pc

    def to_native(self, value):
        value['success'] = _(u'The code has been successfully sent')
        return value
