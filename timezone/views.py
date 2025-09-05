from rest_framework import viewsets, filters
from .models import Timezone
from .serializers import TimezoneEntrySerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated

class TimezoneEntryViewSet(viewsets.ModelViewSet):
    serializer_class = TimezoneEntrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'city']

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'manager']:
            return Timezone.objects.all()
        return Timezone.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
