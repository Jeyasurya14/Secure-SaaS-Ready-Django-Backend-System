from rest_framework import serializers
from .models import APILog

class APILogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = APILog
        fields = '__all__'
