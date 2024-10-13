from django import forms
from .models import Book, Card, Record


class CardForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Card
        fields = "__all__"


class BookForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Book
        fields = "__all__"


class RecordForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Record
        fields = "__all__"
