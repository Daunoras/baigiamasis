from django import forms
from django.contrib.auth.models import User
from .models import Plant

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomPlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'pic', 'watered', 'watering', 'sciname', 'owner']
        widgets = {'owner': forms.HiddenInput(), 'watered': DateInput()}
