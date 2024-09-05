from rest_framework import serializers
from .models import Profiles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ['id', 'email', 'username', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ['email', 'username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Profiles.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        return user
