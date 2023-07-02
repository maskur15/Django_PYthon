from django.forms import ModelForm 
from .models import Papers
class paperForm(ModelForm):
    class Meta: 
        model = Papers 
        fields = '__all__'
    
    def __init__(self,*args,**kwargs):
        super(paperForm,self).__init__(*args,**kwargs)
        for key,value in self.fields.items():
            value.widget.attrs.update({'class': 'input'})
       # self.fields['title'].widget.attrs.update({'class':'input'})
