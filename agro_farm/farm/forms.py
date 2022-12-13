from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1','password2']

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


