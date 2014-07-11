# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea

from pythonbrasil8.dashboard.models import AccountProfile


class ProfileForm(ModelForm):

    class Meta:
        model = AccountProfile
        fields = ('name', 'description', 'twitter', 'public',)
        widgets = {
            'description': Textarea,
        }


class SpeakerProfileForm(ProfileForm):

    class Meta(ProfileForm.Meta):
        exclude = ('user', 'payement', 'type')
