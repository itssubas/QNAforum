from django import forms
from about.models import Feedback

class FeedbackForm(forms.ModelForm):
    your_message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Feedback
        fields = ['your_name', 'your_email', 'your_message']
