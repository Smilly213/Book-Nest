from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'full_name', 'birth_date', 'context')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }