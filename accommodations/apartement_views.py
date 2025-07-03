from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Apartment
from .serializers import ApartmentSerializer


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
