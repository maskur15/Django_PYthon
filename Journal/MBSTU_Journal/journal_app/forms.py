from django.forms import ModelForm 
from .models import Papers
class paperForm(ModelForm):
    class Meta: 
        model = Papers 
        fields = '__all__'

