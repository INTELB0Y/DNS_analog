from django import forms
from .models import Task

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__' #['title']
        widget = {
            'about': forms.Textarea(
                attrs={
                    'placeholder': 'Input about',
                    'row': 5,
                    'class': 'form__about'
                }
            )
        }