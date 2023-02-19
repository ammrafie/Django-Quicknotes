from django import forms
from django.core.exceptions import ValidationError
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {'text': 'Write your thoughts:'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-1'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-1'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("Only title containing `Django` is accepted")
        return title
