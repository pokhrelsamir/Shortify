from django.db import models


class ShortURL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=10, unique=True)
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"