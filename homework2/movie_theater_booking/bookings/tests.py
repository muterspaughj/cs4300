from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from datetime import date

from .models import Movie, Seat, Booking


class MovieModelTest(TestCase):

    def setUp(self):
        # Create a sample movie
        self.movie = Movie.objects.create(
            title="Interstellar",
            description="A science fiction movie.",
            release_date=date(2014, 11, 7),
            duration=169
        )

    def test_movie_creation(self):
        # Check that the movie was saved
        self.assertEqual(self.movie.title, "Interstellar")
        self.assertEqual(self.movie.duration, 169)

    def test_movie_string(self):
        # Check the movie's string representation
        self.assertEqual(str(self.movie), "Interstellar")


class SeatModelTest(TestCase):

    def setUp(self):
        # Create a sample seat
        self.seat = Seat.objects.create(
            seat_number="A1",
            is_booked=False
        )

    def test_seat_creation(self):
        # Check the seat number
        self.assertEqual(self.seat.seat_number, "A1")

    def test_seat_available(self):
        # New seats should be available
        self.assertFalse(self.seat.is_booked)


class BookingModelTest(TestCase):

    def setUp(self):
        # Create test user, movie, and seat
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.movie = Movie.objects.create(
            title="The Dark Knight",
            description="A Batman movie.",
            release_date=date(2008, 7, 18),
            duration=152
        )

        self.seat = Seat.objects.create(
            seat_number="A1"
        )

    def test_booking_creation(self):
        # Create a booking
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

        # Verify booking details
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat)
        self.assertEqual(booking.user, self.user)

    def test_duplicate_booking(self):
        # Book a seat for a movie
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

        # Booking the same seat again should fail
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Booking.objects.create(
                    movie=self.movie,
                    seat=self.seat,
                    user=self.user
                )

    def test_same_seat_different_movie(self):
        # A seat can be booked for another movie
        other_movie = Movie.objects.create(
            title="Inception",
            description="A science fiction thriller.",
            release_date=date(2010, 7, 16),
            duration=148
        )

        Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

        second_booking = Booking.objects.create(
            movie=other_movie,
            seat=self.seat,
            user=self.user
        )

        self.assertEqual(second_booking.movie, other_movie)


class BookingAPITest(APITestCase):

    def setUp(self):
        # Create a user for API testing
        self.user = User.objects.create_user(
            username="apiuser",
            password="testpass123"
        )

        # Create a sample movie
        self.movie = Movie.objects.create(
            title="Inception",
            description="A science fiction thriller.",
            release_date=date(2010, 7, 16),
            duration=148
        )

        # Create a sample seat
        self.seat = Seat.objects.create(
            seat_number="B1"
        )

    def test_get_movies(self):
        # Verify the movie API returns movie data
        response = self.client.get('/api/movies/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(response.data), 1)

    def test_create_movie(self):
        # Test adding a movie through the API
        data = {
            "title": "The Matrix",
            "description": "A science fiction movie.",
            "release_date": "1999-03-31",
            "duration": 136
        }

        response = self.client.post(
            '/api/movies/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(Movie.objects.count(), 2)

    def test_get_seats(self):
        # Verify the seat API returns seat data
        response = self.client.get('/api/seats/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        # Log in before creating a booking
        self.client.force_authenticate(user=self.user)

        data = {
            "movie": self.movie.id,
            "seat": self.seat.id
        }

        response = self.client.post(
            '/api/bookings/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(Booking.objects.count(), 1)

    def test_duplicate_booking_api(self):
        # Authenticate the test user
        self.client.force_authenticate(user=self.user)

        data = {
            "movie": self.movie.id,
            "seat": self.seat.id
        }

        # First booking should succeed
        first_response = self.client.post(
            '/api/bookings/',
            data,
            format='json'
        )

        # Second booking should fail
        second_response = self.client.post(
            '/api/bookings/',
            data,
            format='json'
        )

        self.assertEqual(
            first_response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            second_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_booking_requires_login(self):
        # Unauthenticated users cannot book seats
        response = self.client.post(
            '/api/bookings/',
            {
                "movie": self.movie.id,
                "seat": self.seat.id
            },
            format='json'
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN
            ]
        )

    def test_booking_history(self):
        # Create a booking for the test user
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

        # Request the user's booking history
        response = self.client.get('/api/bookings/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(response.data), 1)
