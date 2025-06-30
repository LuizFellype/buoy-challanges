from rest_framework import serializers
from .models import Accommodation, Hotel, Apartment


class AccommodationSerializer(serializers.ModelSerializer):
    """Serializer for Accommodation model"""
    
    class Meta:
        model = Accommodation
        fields = ['id', 'name', 'description', 'price', 'location']
        read_only_fields = ['id']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value

    def validate_location(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Location must be at least 2 characters")
        return value


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'description', 'price', 'location', 'number_of_rooms']
        read_only_fields = ['id']


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id', 'name', 'description', 'price', 'location', 'floor_number']
        read_only_fields = ['id']