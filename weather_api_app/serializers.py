from rest_framework import serializers
from .models import City

class CItySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'