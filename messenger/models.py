from django.conf import settings
from django.db import models


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="messages"
    )

    @property
    def text_preview(self):
        return self.text[:20] + "..."

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
