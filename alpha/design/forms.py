from django import forms
from .models import *

class applyform(forms.ModelForm):
    class Meta:
        model = Apply
        fields = "__all__"
