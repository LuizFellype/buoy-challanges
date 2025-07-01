from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Accommodation, Hotel, Apartment
from .serializers import AccommodationSerializer, HotelSerializer, ApartmentSerializer

# Accomodations
class AccommodationListCreateView(generics.ListCreateAPIView):
    """List all accommodations or create a new accommodation"""
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

    @extend_schema(
        summary="List all accommodations",
        description="Get a list of all accommodations",
        tags=["Accommodations"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new accommodation",
        description="Create a new accommodation",
        tags=["Accommodations"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class AccommodationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an accommodation"""
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

    @extend_schema(
        summary="Get accommodation by ID",
        description="Retrieve a specific accommodation by its ID",
        tags=["Accommodations"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update accommodation",
        description="Update a specific accommodation",
        tags=["Accommodations"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Delete accommodation",
        description="Delete a specific accommodation",
        tags=["Accommodations"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Hotels
class HotelListCreateView(generics.ListCreateAPIView):
    """List all Hotels or create a new one"""
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

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


# Apartments
class ApartmentListCreateView(generics.ListCreateAPIView):
    """List all Apartments or create a new one"""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    @extend_schema(
        summary="List all Apartments",
        description="Get a list of all Apartments",
        tags=["Apartments"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new Apartments",
        description="Create a new Apartments",
        tags=["Apartments"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ApartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an Apartment"""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    @extend_schema(
        summary="Get Apartment by ID",
        description="Retrieve a specific Apartment by its ID",
        tags=["Apartments"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update Apartment",
        description="Update a specific Apartment",
        tags=["Apartments"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Delete Apartment",
        description="Delete a specific Apartment",
        tags=["Apartments"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
