from django.db import models
from accommodations.models import Accommodation
from datetime import timedelta


class Booking(models.Model):
    """Booking model"""
    accommodation = models.ForeignKey(
        Accommodation, 
        on_delete=models.CASCADE, 
        related_name='bookings'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return f"{self.guest_name} - {self.accommodation.name} ({self.start_date} to {self.end_date})"

    def has_overlap(self):
        """Check if the booking overlaps with existing bookings"""
        overlapping_bookings = Booking.objects.filter(
            accommodation=self.accommodation,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exists()
        
        return overlapping_bookings

    @staticmethod
    def get_next_available_date(accommodation, date):
        """Get the next available date for an accommodation"""
        bookings = Booking.objects.filter(
            accommodation=accommodation,
            end_date__gte=date
        ).order_by('end_date')
        
        if bookings.exists():
            one_day_diff = timedelta(days=1)
            
            for current_booking, next_booking in zip(bookings, bookings[1:]):
                gap_between_bookings = (current_booking.end_date - next_booking.start_date) > one_day_diff
                if (gap_between_bookings):
                    return current_booking.end_date + one_day_diff
        
            return bookings.last().end_date + one_day_diff
        
        return date
