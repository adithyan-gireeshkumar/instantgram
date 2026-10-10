from rest_framework import serializers
from .models import Automation

class AutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automation
        fields = [
            "id",
            "user",
            "instagram_account",
            "name",
            "description",
            "trigger_type",
            "keyword",
            "response_text",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id","user", "created_at", "updated_at"]