from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    password_hash = serializers.CharField(max_length=100, required=True, write_only=True)
    age = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            password_hash=validated_data['password_hash'],
            age=validated_data['age']
        )
        return user
