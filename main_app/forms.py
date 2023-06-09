from django.forms import ModelForm
from .models import ReadingList


class ReadingListForm(ModelForm):
    class Meta:
        model = ReadingList
        fields = ['category']
