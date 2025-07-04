from rest_framework import generics
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from accommodations.models import Accommodation
from datetime import datetime
from .models import Booking
from .serializers import BookingSerializer
from src.helpers.pagination import IDCursorPagination


class BookingListCreateView(generics.ListCreateAPIView):
    """List all bookings or create a new booking"""
    queryset = Booking.objects.select_related('accommodation').all()
    serializer_class = BookingSerializer
    pagination_class = IDCursorPagination

    @extend_schema(
        summary="List all bookings",
        description="Get a list of all bookings",
        tags=["Bookings"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new booking",
        description="Create a new booking for an accommodation",
        tags=["Bookings"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a booking"""
    queryset = Booking.objects.select_related('accommodation').all()
    serializer_class = BookingSerializer

    @extend_schema(
        summary="Get booking by ID",
        description="Retrieve a specific booking by its ID",
        tags=["Bookings"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update booking",
        description="Update a specific booking",
        tags=["Bookings"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Delete booking",
        description="Delete a specific booking",
        tags=["Bookings"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class NextAvailableDateView(APIView):
    """Retrieve the next available date for an accommodation"""
    
    @extend_schema(
        summary="Get date availability",
        description="Get Next available date for an accommodation",
        parameters=[
            OpenApiParameter(
                name="accommodation_id",
                description=(
                    "ID of the accomodation to search for its abailability"
                ),
                type=int,
            ),
             OpenApiParameter(
                name="date",
                description=(
                    "Starting point date - recommended format: yyyy/mm/dd"
                ),
                type=str,
            )
        ],
        tags=["Bookings"]
    )
    def get(self, request):
        accommodation_id = request.GET.get('accommodation_id')
        date = request.GET.get('date')

        if not accommodation_id or not date:
            return Response({'error': 'Missing accommodation_id or date query parameter'}, status=400)

        try:
            accommodation = Accommodation.objects.get(id=accommodation_id)
        except Accommodation.DoesNotExist:
            return Response({'error': 'Accommodation not found'}, status=404)

        try:
            parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        next_date = Booking.get_next_available_date(accommodation, parsed_date)
        return Response({'next_available_date': next_date})
    