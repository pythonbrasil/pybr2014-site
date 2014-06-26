# coding: utf-8

import responses

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

from model_mommy import mommy
from rest_framework.permissions import AllowAny
from rest_framework.test import APIRequestFactory

from pythonbrasil8.promo_code import views


factory = APIRequestFactory()


class PromoCodeViewTestCase(TestCase):
    def setUp(self):
        self.pc = mommy.make('promo_code.PromoCode', email=None)

        self.mock_kwargs = {
            'method': responses.GET, 'content_type': 'application/json',
            'body': '{"status": "active"}', 'status': 200,
            'url': 'http://associados.python.org.br/members/status/',
        }

        self.view = views.PromoCodeView.as_view()

    def test_view_url(self):
        url = reverse('promo_code:request_code')
        response = self.client.post(url, data={'email': ''})
        self.assertEqual(response.status_code, 400)

    def test_should_not_require_authentication(self):
        self.assertEqual(
            views.PromoCodeView.permission_classes,
            [AllowAny],
        )

    def test_should_return_400_on_validation_error(self):
        request = factory.post('/', data={'email': ''}, format='json')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 400)

    @responses.activate
    def test_should_return_200_on_success(self):
        responses.add(**self.mock_kwargs)

        request = factory.post('/', data={'email': 'a@a.com'}, format='json')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 200)

    @responses.activate
    def test_valid_request_should_mail_user_code(self):
        responses.add(**self.mock_kwargs)

        request = factory.post('/', data={'email': 'a@a.com'}, format='json')
        self.view(request).render()

        self.assertEqual(
            mail.outbox[0].subject,
            u'Get your PythonBrasil[10] promotional code',
        )
        self.assertIn(self.pc.code, mail.outbox[0].body)
