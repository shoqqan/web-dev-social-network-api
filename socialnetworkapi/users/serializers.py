from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        from django.contrib.auth.models import User
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user