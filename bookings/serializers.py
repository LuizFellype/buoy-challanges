from rest_framework import serializers
from .models import Booking
from accommodations.models import Accommodation, Apartment


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    accommodation_id = serializers.IntegerField(write_only=True)
    accommodation = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'accommodation_id', 'accommodation', 'start_date', 
                 'end_date', 'guest_name']
        read_only_fields = ['id', 'accommodation']

    def validate_accommodation_id(self, value):
        """Validate accommodation exists"""
        try:
            Accommodation.objects.get(id=value)
        except Accommodation.DoesNotExist:
            raise serializers.ValidationError("Invalid accommodation ID")
        return value

    def validate_guest_name(self, value):
        """Validate guest name length"""
        if len(value) < 2:
            raise serializers.ValidationError("Guest name must be at least 2 characters")
        return value

    def validate(self, data):
        """Cross-field validation"""
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError("End date must be after start date")
        
        try:
            apartment = Apartment.objects.get(id=data['accommodation_id'])

            overlapping = Booking(
                accommodation=apartment,
                start_date=data['start_date'],
                end_date=data['end_date']
            ).has_overlap()
            
            if overlapping:
                raise serializers.ValidationError("Overlapping bookings are not allowed for apartments.")
        
            return data
        except Apartment.DoesNotExist:
            return data
        

    def create(self, validated_data):
        """Create booking with accommodation"""
        accommodation_id = validated_data.pop('accommodation_id')
        accommodation = Accommodation.objects.get(id=accommodation_id)
        
        booking = Booking(accommodation=accommodation, **validated_data)
        booking.save()
        return booking 