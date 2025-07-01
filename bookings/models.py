from django.db import models
from accommodations.models import Accommodation


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