from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Movie, Seat, Booking
from .serializers import (
    MovieSerializer,
    SeatSerializer,
    BookingSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user
        ).order_by('-booking_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        raise PermissionDenied(
            "Bookings cannot be modified. Cancel and rebook instead."
        )

