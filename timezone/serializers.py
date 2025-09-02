from rest_framework import serializers
from .models import TimezoneEntry
from users.models import User  # Assuming you have a custom User model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class TimezoneEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TimezoneEntry
        fields = ['id', 'user', 'name', 'city', 'gmt_offset', 'created_at', 'updated_at']
