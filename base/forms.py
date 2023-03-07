from dataclasses import field, fields
from pyexpat import model
from traceback import format_tb
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter room name...',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter room description...'
            })
        }


class TopicForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Topic


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'picture', 'username',
                  'email', 'about', 'password1', 'password2']


class MessageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type something...'
    }))

    class Meta:
        model = Message
        fields = ['body',]


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'picture',
            'username',
            'about',
            'email',
        ]
