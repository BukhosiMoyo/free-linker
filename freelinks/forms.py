from django import forms
from .models import Link, LinkProject


class LinkCreateForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields = ('name', 'link')
        
        
            
class ProjectCreateForm(forms.ModelForm):
    
    class Meta:
        model = LinkProject
        fields = ("project_name",)