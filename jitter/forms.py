from django.forms import ModelForm
from django import forms
from .models import Bunk, User
from django.utils import timezone

class bunkSomeoneForm(forms.Form):
    fromUser = forms.ModelChoiceField(queryset=User.objects.all(), label="Person doing the bunking")
    toUser = forms.ModelChoiceField(queryset=User.objects.all(), label="Person being bunked")