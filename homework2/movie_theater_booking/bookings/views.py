from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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
    
def movie_list(request):
        movies = Movie.objects.all().order_by('title')

        return render(
            request,
            'bookings/movie_list.html',
            {'movies': movies}
    )


# Require users to log in before booking
@login_required
def book_seat(request, movie_id):
    # Get the selected movie
    movie = get_object_or_404(Movie, id=movie_id)

    # Find seats already booked for this movie
    booked_seat_ids = set(
        Booking.objects.filter(movie=movie)
        .values_list('seat_id', flat=True)
    )

    # Get all theater seats
    seats = Seat.objects.all().order_by('seat_number')

    # Handle a booking submission
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)

        try:
            # Save the booking to the database
            with transaction.atomic():
                Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user=request.user
                )

            # Show a success message
            messages.success(
                request,
                f"Successfully booked seat {seat.seat_number} "
                f"for {movie.title}!"
            )
            return redirect('booking_history')

        except IntegrityError:
            # Handle seats that are already booked
            messages.error(
                request,
                "This seat is already booked. Please select another."
            )
            return redirect('book_seat', movie_id=movie.id)

    # Mark each seat as available or booked
    seat_data = [
        {
            'id': seat.id,
            'number': seat.seat_number,
            'booked': seat.id in booked_seat_ids
        }
        for seat in seats
    ]

    # Display the seat selection page
    return render(
        request,
        'bookings/seat_booking.html',
        {
            'movie': movie,
            'seats': seat_data
        }
    )


# Display the logged-in user's booking history
@login_required
def booking_history(request):
    # Get the user's bookings, newest first
    bookings = (
        Booking.objects.filter(user=request.user)
        .select_related('movie', 'seat')
        .order_by('-booking_date')
    )

    # Display the booking history page
    return render(
        request,
        'bookings/booking_history.html',
        {'bookings': bookings}
    )

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
