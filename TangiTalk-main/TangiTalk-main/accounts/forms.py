from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField
)

from django import forms
from django.contrib.auth.models import User
from .models import Profile




class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=_("Username"),
        widget=forms.TextInput(
            attrs={
                'placeholder': "Username",
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        max_length=255, 
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Password",
                'class': 'form-control'
            }
        )
    )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=255, 
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Password"
            }
        )
    )
    password2 = forms.CharField(
        max_length=255, 
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Confirm Password"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['description', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.user = user
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        if hasattr(self, 'user'):
            profile.user = self.user
            profile.user.first_name = self.cleaned_data['first_name']
            profile.user.last_name = self.cleaned_data['last_name']
            profile.user.save()
        if commit:
            profile.save()
        return profile
