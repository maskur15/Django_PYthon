from django.forms import ModelForm
from .models import Projects

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields='__all__'
        exclude=['vote_total','vote_ratio']