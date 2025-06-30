from django.urls import path
from .views import AccommodationListCreateView, AccommodationDetailView, HotelListCreateView, HotelDetailView, ApartmentListCreateView, ApartmentDetailView

urlpatterns = [
    path('', AccommodationListCreateView.as_view(), name='accommodation-list-create'),
    path('<int:pk>/', AccommodationDetailView.as_view(), name='accommodation-detail'),
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('apartments/', ApartmentListCreateView.as_view(), name='apartment-list-create'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
]