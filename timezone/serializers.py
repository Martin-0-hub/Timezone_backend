from rest_framework import serializers
from .models import Timezone 
from users.models import User  # Assuming you have a custom User model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class TimezoneEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ["id", "user", "name", "city", "gmt_diff", "created_at", "updated_at"]
        read_only_fields = ["user", "created_at", "updated_at"]