from rest_framework import serializers
from app_users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ['username']