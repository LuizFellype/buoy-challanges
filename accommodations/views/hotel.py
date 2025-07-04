from rest_framework import generics
from drf_spectacular.utils import extend_schema
from ..models import Hotel
from ..serializers import HotelSerializer
from src.helpers.pagination import IDCursorPagination


# Hotels
class HotelListCreateView(generics.ListCreateAPIView):
    """List all Hotels or create a new one"""
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = IDCursorPagination


    @extend_schema(
        summary="List all Hotels",
        description="Get a list of all Hotels",
        tags=["Hotels"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new Hotels",
        description="Create a new Hotels",
        tags=["Hotels"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an Hotel"""
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @extend_schema(
        summary="Get Hotel by ID",
        description="Retrieve a specific Hotel by its ID",
        tags=["Hotels"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update Hotel",
        description="Update a specific Hotel",
        tags=["Hotels"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Delete Hotel",
        description="Delete a specific Hotel",
        tags=["Hotels"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

