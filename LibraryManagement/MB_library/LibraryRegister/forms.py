from django.forms import ModelForm
from .models import Book
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields='__all__'
        exclude=['vote_total','vote_ratio','id']
