from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=8)
    repeat_password = forms.CharField(min_length=8)
    age = forms.IntegerField(max_value=3)
