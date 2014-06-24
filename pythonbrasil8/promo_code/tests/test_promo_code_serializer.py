# coding: utf-8

import requests
import responses
from mock import patch

from django.test import TestCase

from model_mommy import mommy

from pythonbrasil8.promo_code.serializers import PromoCodeSerializer


class PromoCodeSerializerTestCase(TestCase):
    def setUp(self):
        mommy.make('promo_code.PromoCode', email=None)

        self.mock_kwargs = {
            'method': responses.GET, 'content_type': 'application/json',
            'body': '{"status": "active"}', 'status': 200,
            'url': 'http://associados.python.org.br/members/status/',
        }

    @responses.activate
    def test_should_return_success_message_on_success(self):
        responses.add(**self.mock_kwargs)
        ser = PromoCodeSerializer(data={'email': 'foo@bar.com'})
        self.assertTrue(ser.is_valid())
        self.assertEqual(
            ser.data['success'], u'The code has been successfully sent',
        )

    @responses.activate
    def test_should_not_assign_email_to_promo_code_if_email_exists(self):
        responses.add(**self.mock_kwargs)

        pc = mommy.make('promo_code.PromoCode', email='foo@bar.com')
        ser = PromoCodeSerializer(data={'email': 'foo@bar.com'})
        self.assertTrue(ser.is_valid())
        new_pc = ser.save()
        self.assertEqual(pc.pk, new_pc.pk)

    @responses.activate
    def test_should_assign_email_to_promo_code_if_emails_does_not_exists(self):
        responses.add(**self.mock_kwargs)

        ser = PromoCodeSerializer(data={'email': 'foo@bar.com'})
        self.assertTrue(ser.is_valid())
        new_pc = ser.save()
        self.assertEqual(new_pc.email, 'foo@bar.com')

    @responses.activate
    def test_should_raise_error_if_not_associated(self):
        self.mock_kwargs['body'] = '{"status": false}'
        responses.add(**self.mock_kwargs)

        ser = PromoCodeSerializer(data={'email': 'foo@bar.com'})
        self.assertFalse(ser.is_valid())
        self.assertEqual(
            ser.errors['email'][0], u'E-mail is not valid associated email',
        )

    def test_should_raise_third_party_error_if_connection_error(self):
        ser = PromoCodeSerializer(data={'email': 'foo@bar.com'})

        with patch.object(requests, 'get') as m:
            m.side_effect = requests.exceptions.ConnectionError

            self.assertFalse(ser.is_valid())
            self.assertEqual(
                ser.errors['email'][0],
                u'Problem connecting with third party service',
            )
