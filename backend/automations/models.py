from django.conf import settings
from django.db import models

class Automation(models.Model):
    class TrigerType(models.TextChoices):
        COMMENT = "comment", "Comment"
        DIRECT_MESSAGE = "direct_message", "Direct Message"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="automations",
    )    
    instagram_account = models.ForeignKey(
        "instagram.InstagramAccount",
        on_delete=models.CASCADE,
        related_name="automations",
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    trigger_type = models.CharField(max_length=20, choices=TrigerType.choices)
    keyword = models.CharField(max_length=150)
    response_text = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
