# forms.py
from django import forms
from .models import SubProfile

class SubProfileForm(forms.ModelForm):
    class Meta:
        model = SubProfile
        fields = ['nickname', 'balance', 'exposure_limit', 'is_active', 'is_suspended', 'is_locked']
        widgets = {
            'balance': forms.NumberInput(attrs={'step': '0.01'}),
            'exposure_limit': forms.NumberInput(attrs={'step': '0.01'}),
        }
