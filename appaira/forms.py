"""forms for app are defined here"""
from django import forms
from .models import AiraUser

class AiraUserform(forms.ModelForm):
    """form for airaapp users"""
    class Meta:
        """meta for forms"""
        model = AiraUser
        fields = ['email', 'username','first_name', 'last_name', 'password', 'phone_number']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        