from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","role"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, validators = [validate_password])
    role = serializers.ChoiceField(choices=User.Roles.choices, required = False)

    class Meta:
        model = User
        fields = ["username","email","password","first_name","last_name","role"]

    def create(self,validated_data):
        role = validated_data.pop("role",User.Roles.REGULAR)
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.role = role
        user.save()
        return user
    
    def validate_role(self,value):
        return User.Role.REGULAR