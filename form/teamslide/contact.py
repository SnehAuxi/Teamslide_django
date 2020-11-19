from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import MemberName

class ContactForm(forms.Form):
    num_members = forms.CharField(max_length=100, label='How many members?')

class NameForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Enter the name: ')

    class Meta:
        model = MemberName
        fields = ('name',)

