from django import forms
from django.utils import timezone

from .models import ShortURL


class ShortURLForm(forms.ModelForm):

    EXPIRATION_CHOICES = [
        ("never", "Never"),
        ("1h", "1 hour"),
        ("1d", "1 day"),
        ("7d", "7 days"),
        ("30d", "30 days"),
    ]

    expiration = forms.ChoiceField(
        choices=EXPIRATION_CHOICES,
        initial="never",
        widget=forms.Select(
            attrs={
                "class": "expiration-select",
            }
        ),
        label="Expiration",
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
        }

    def save(self, commit=True):
        link = super().save(commit=False)

        expiration = self.cleaned_data.get("expiration")

        now = timezone.now()

        if expiration == "1h":
            link.expires_at = now + timezone.timedelta(hours=1)

        elif expiration == "1d":
            link.expires_at = now + timezone.timedelta(days=1)

        elif expiration == "7d":
            link.expires_at = now + timezone.timedelta(days=7)

        elif expiration == "30d":
            link.expires_at = now + timezone.timedelta(days=30)

        else:
            link.expires_at = None

        if commit:
            link.save()

        return link