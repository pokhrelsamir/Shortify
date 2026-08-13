import secrets
import string

from django.db import models
from django.utils import timezone


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


class ShortURL(models.Model):
    original_url = models.URLField(max_length=2048)

    short_code = models.CharField(
        max_length=10,
        unique=True,
    )

    clicks = models.PositiveIntegerField(
        default=0
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Short URL"

        verbose_name_plural = "Short URLs"

    @property
    def is_expired(self):
        """
        Returns True when the link has passed its expiration time.
        Links without an expiration date never expire.
        """
        if self.expires_at is None:
            return False

        return timezone.now() >= self.expires_at

    @property
    def is_expiring(self):
        """
        Returns True when the link has an expiration date
        and that date has not been reached yet.
        """
        if self.expires_at is None:
            return False

        if self.is_expired:
            return False

        return True

    def save(self, *args, **kwargs):
        if not self.short_code:
            while True:
                code = generate_short_code()

                if not ShortURL.objects.filter(
                    short_code=code
                ).exists():
                    self.short_code = code
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"