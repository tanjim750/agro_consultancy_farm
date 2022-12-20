from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.core import validators

class password_reset_form(forms.Form):
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1','password2']

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


