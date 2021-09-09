from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'state',
            'address1',
            'address2',
            'zip',
        )
        model = CustomUser