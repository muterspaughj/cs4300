from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import SignUpView

from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
]
