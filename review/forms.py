from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    pdf_file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control", "accept": ".pdf,application/pdf"}
        ),
    )

    class Meta:
        model = Feedback
        exclude = ["user"]
        fields = ["woreda", "comments", "pdf_file"]
        widgets = {
            "woreda": forms.TextInput(attrs={"class": "form-control"}),
            "comments": forms.Textarea(attrs={"class": "form-control"}),
        }
