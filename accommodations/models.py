from django.db import models


class Accommodation(models.Model):
    """Accommodation model"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'accommodation'

    def __str__(self):
        return self.name


class Hotel(Accommodation):
    """Hotel model inheriting Accommodation"""
    number_of_rooms = models.PositiveIntegerField()

    class Meta:
        db_table = 'hotel'


class Apartment(Accommodation):
    """Apartment model inheriting Accommodation"""
    floor_number = models.PositiveIntegerField()

    class Meta:
        db_table = 'apartment'