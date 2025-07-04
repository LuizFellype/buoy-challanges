from django.db import models
from .accommodation import Accommodation

class Apartment(Accommodation):
    """Apartment model inheriting Accommodation"""
    floor_number = models.PositiveIntegerField()

    class Meta:
        db_table = 'apartment'