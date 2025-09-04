from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

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
        return User.Roles.REGULAR
    
class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD  # make DRF-SimpleJWT use email

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email is None or password is None:
            raise serializers.ValidationError("Must include email and password.")

        # authenticate using email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid credentials.")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
            }
        }