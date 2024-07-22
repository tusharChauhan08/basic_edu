from django import forms
from .models import *

class AddData(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

