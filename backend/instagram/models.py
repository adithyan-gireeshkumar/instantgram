from django.conf import settings
from django.db import models


class InstagramAccount(models.Model):
    class ConnectionStatus(models.TextChoices):
        CONNECTED = "connected", "Connected"
        DISCONNECTED = "disconnected", "Disconnected"
        EXPIRED = "expired", "Token Expired"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="instagram_accounts",
    )
    instagram_user_id = models.CharField(
        max_length=100,
        unique=True,
    )
    username = models.CharField(max_length=150)
    account_name = models.CharField(max_length=255, blank=True)
    connection_status = models.CharField(
        max_length=20,
        choices=ConnectionStatus.choices,
        default=ConnectionStatus.DISCONNECTED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"@{self.username}"