from django.forms import ModelForm
from .models import Link


class LinkCreateForm(ModelForm):
    
    class Meta:
        model = Link
        fields = ('name', 'link', 'project',)
        
        
            