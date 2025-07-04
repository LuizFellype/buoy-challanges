from django.db import models
from .accommodation import Accommodation

class Hotel(Accommodation):
    """Hotel model inheriting Accommodation"""
    number_of_rooms = models.PositiveIntegerField()

    class Meta:
        db_table = 'hotel'
