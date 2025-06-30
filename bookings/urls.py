from django.urls import path
from .views import BookingListCreateView, BookingDetailView, NextAvailableDateView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('<int:accommodation_id>/next-available-date/<str:date>/', NextAvailableDateView.as_view(), name='next-available-date'),
]