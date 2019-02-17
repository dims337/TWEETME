from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            #"user",
            "content"
        ]
     #personalizing validation of our content
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if content == "":
            raise forms.ValidationError('cannot be blank')
        return content