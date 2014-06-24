# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from pythonbrasil8.promo_code import views


urlpatterns = patterns('',
    url(r'^$', views.PromoCodeView.as_view(), name='request_code'),
)
