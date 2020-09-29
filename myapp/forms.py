from django import forms
from django.core import validators
class DevoteeRegister(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    Feedback=forms.CharField(widget=forms.Textarea)
class feedbackform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    Feedback=forms.CharField(widget=forms.Textarea)
def clean_name(self):
    inputname=self.cleaned_data['name']
    if len(inputname)<4:
        raiseforms.ValidationError('the length shd be min 4 charecters')
    return inputname
