from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)
    again_pwd = forms.CharField(max_length=32)
    email = forms.CharField(max_length=64)
    mobile_phone = forms.CharField(max_length=12)


