from .models import TODO
from django import forms

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'contents']
        lables = {'title': 'Title',
                   'contents': 'Contents'}

        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Enter title here','class': 'form-control mb-3'}),
                   'contents': forms.TextInput(attrs={'placeholder': 'Enter contents here','class': 'form-control mb-3'})
                   }
