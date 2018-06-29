from django import forms

from .models import *

class UploadConfirmForm(forms.Form):
	cookie = forms.CharField(widget=forms.TextInput({'class':'form-control', 'placeholder':'Cookie...',}))