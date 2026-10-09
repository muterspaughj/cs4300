
from behave import given, when, then
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from datetime import date

from bookings.models import Movie, Seat, Booking


@given('a movie and an available seat exist')
def step_available_seat(context):
    # Create test data
    context.user = User.objects.create_user(
        username='bdduser1',
        password='testpass123'
    )

    context.movie = Movie.objects.create(
        title='Interstellar',
        description='Science fiction',
        release_date=date(2014, 11, 7),
        duration=169
    )

    context.seat = Seat.objects.create(
        seat_number='A1'
    )


@when('a user books the available seat')
def step_book_seat(context):
    # Create a reservation
    context.booking = Booking.objects.create(
        movie=context.movie,
        seat=context.seat,
        user=context.user
    )


@then('the booking should be created')
def step_booking_created(context):
    # Verify the reservation exists
    assert Booking.objects.filter(
        id=context.booking.id
    ).exists()


@given('a movie seat is already booked')
def step_already_booked(context):
    # Create an existing reservation
    step_available_seat(context)

    Booking.objects.create(
        movie=context.movie,
        seat=context.seat,
        user=context.user
    )


@when('another user attempts to book the same seat')
def step_duplicate_attempt(context):
    # Attempt to reserve an occupied seat
    other_user = User.objects.create_user(
        username='bdduser2',
        password='testpass123'
    )

    context.duplicate_rejected = False

    try:
        with transaction.atomic():
            Booking.objects.create(
                movie=context.movie,
                seat=context.seat,
                user=other_user
            )
    except IntegrityError:
        context.duplicate_rejected = True


@then('the duplicate booking should be rejected')
def step_duplicate_rejected(context):
    # Verify the database rejected the duplicate
    assert context.duplicate_rejected
    assert Booking.objects.filter(
        movie=context.movie,
        seat=context.seat
    ).count() == 1


@given('two movies and an available seat exist')
def step_two_movies(context):
    # Create the first movie and seat
    step_available_seat(context)

    # Create another movie
    context.second_movie = Movie.objects.create(
        title='Inception',
        description='Science fiction thriller',
        release_date=date(2010, 7, 16),
        duration=148
    )


@when('the seat is booked for both movies')
def step_book_both(context):
    # Book the same seat for different movies
    Booking.objects.create(
        movie=context.movie,
        seat=context.seat,
        user=context.user
    )

    Booking.objects.create(
        movie=context.second_movie,
        seat=context.seat,
        user=context.user
    )


@then('both bookings should be created')
def step_both_created(context):
    # Verify both reservations exist
    assert Booking.objects.filter(
        seat=context.seat
    ).count() == 2
