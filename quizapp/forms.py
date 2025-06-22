from django import forms
from .models import questions

class questionform(forms.ModelForm):
    class Meta:
        model = questions
        fields = "__all__"
