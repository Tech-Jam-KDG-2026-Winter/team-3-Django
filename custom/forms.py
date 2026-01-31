from django import forms
from .models import SetMenu

class SetMenuForm(forms.ModelForm):
    class Meta:
        model = SetMenu
        fields = [
            'weekday',
            'menu',
            'level',
            'starttime'
            ]
        labels = {
            'weekday':'曜日',
            'menu': 'やること',
            'level': '強度',
            'starttime': '開始時間',
        }
        widgets = {
            'weekday': forms.HiddenInput(),
            'starttime': forms.TimeInput(attrs={'type': 'time'}),
        }