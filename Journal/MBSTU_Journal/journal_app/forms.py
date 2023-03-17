from django.forms import ModelForm 
from .models import Papers
class JournalForm(ModelForm):
    class Meta: 
        model = Papers 
        fields = '__all__'

