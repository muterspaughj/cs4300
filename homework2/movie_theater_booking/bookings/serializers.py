from rest_framework import serializers
from django.db import IntegrityError, transaction
from .models import Movie, Seat, Booking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'seat', 'user', 'booking_date']
        read_only_fields = ['id', 'user', 'booking_date']

    def validate(self, data):
        movie = data['movie']
        seat = data['seat']

        if Booking.objects.filter(movie=movie, seat=seat).exists():
            raise serializers.ValidationError(
                "This seat is already booked for this movie."
            )

        return data

    def create(self, validated_data):
        try:
            with transaction.atomic():
                return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                "This seat is already booked for this movie."
            )
