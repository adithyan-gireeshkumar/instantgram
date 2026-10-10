from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Automation
from .serializers import AutomationSerializer

class AutomationViewSet(viewsets.ModelViewSet):
    serializer_class = AutomationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Automation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    
