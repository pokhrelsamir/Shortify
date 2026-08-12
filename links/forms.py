from django import forms

from .models import ShortURL


class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ["original_url"]

        widgets = {
            "original_url": forms.URLInput(
                attrs={
                    "class": "url-input",
                    "placeholder": "https://example.com/your-long-url",
                    "autocomplete": "off",
                }
            ),
        }

        labels = {
            "original_url": "",
        }