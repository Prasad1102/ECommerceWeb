from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ("id", "username", "email", "first_name", "last_name", "mobile_number")

class UserRegistrationSerializer(serializers.ModelSerializer):
  password1 = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True)

  class Meta:
    model = CustomUser
    fields = ("id", "username", "email", "first_name", "last_name", "mobile_number", "password1", "password2")

  def validate(self, attrs):
    if attrs['password1'] != attrs['password2']:
      raise serializers.ValidationError("Passwords do not match!")
    password = attrs.get("password1", "")
    if len(password) < 8:
      raise serializers.ValidationError("Password length must be more than 8 charecters.")
    return attrs
  
  def create(self, validated_data):
    password = validated_data.pop("password1")
    validated_data.pop("password2")

    return CustomUser.objects.create_user(password=password, **validated_data)
  
class UserLoginSerializer(serializers.Serializer):
  email = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")
  
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = '__all__'