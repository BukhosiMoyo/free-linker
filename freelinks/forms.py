from django import forms
from .models import Link


class LinkCreateForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields = ('name', 'link')
        
        
            