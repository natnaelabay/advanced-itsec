from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    pdf_file = forms.FileField()
    
    class Meta:
        model = Feedback
        fields = ["user", 'woreda', 'comments', 'pdf_file']
        widgets = {
            'woreda': forms.TextInput(attrs={'class':   'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.TextInput(attrs={'class': 'form-control'}),
        }