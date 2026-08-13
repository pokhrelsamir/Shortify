from django import forms

from .models import ShortURL


class ShortURLForm(forms.ModelForm):

    EXPIRATION_CHOICES = [
        ("never", "Never"),
        ("1_day", "1 Day"),
        ("7_days", "7 Days"),
        ("30_days", "30 Days"),
    ]

    expiration = forms.ChoiceField(
        choices=EXPIRATION_CHOICES,
        required=False,
        initial="never",
        widget=forms.Select(
            attrs={
                "class": "expiration-select",
            }
        ),
    )

    class Meta:
        model = ShortURL

        fields = [
            "original_url",
        ]

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
            "expiration": "Expiration",
        }