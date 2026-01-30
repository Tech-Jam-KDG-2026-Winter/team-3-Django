
from django import forms

class PerformanceForm(forms.Form):
    result = forms.CharField(max_length=10)
    menu = forms.CharField(max_length=20)
    level = forms.CharField(max_length=10)
    time = forms.DecimalField()


