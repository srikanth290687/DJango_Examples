from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
