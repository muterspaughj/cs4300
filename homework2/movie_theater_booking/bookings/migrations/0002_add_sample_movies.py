from django.db import migrations
from datetime import date


def add_sample_data(apps, schema_editor):
    Movie = apps.get_model("bookings", "Movie")
    Seat = apps.get_model("bookings", "Seat")

    movies = [
        {
            "title": "Interstellar",
            "description": "A team of astronauts travels through a wormhole to find a new home for humanity.",
            "release_date": date(2014, 11, 7),
            "duration": 169,
        },
        {
            "title": "Inception",
            "description": "A skilled thief enters people's dreams to steal information.",
            "release_date": date(2010, 7, 16),
            "duration": 148,
        },
        {
            "title": "The Dark Knight",
            "description": "Batman faces the Joker as Gotham City descends into chaos.",
            "release_date": date(2008, 7, 18),
            "duration": 152,
        },
        {
            "title": "Oppenheimer",
            "description": "The story of physicist J. Robert Oppenheimer and the development of the atomic bomb.",
            "release_date": date(2023, 7, 21),
            "duration": 180,
        },
        {
            "title": "Dune: Part Two",
            "description": "Paul Atreides joins the Fremen in a struggle for control of Arrakis.",
            "release_date": date(2024, 3, 1),
            "duration": 166,
        },
    ]

    for movie_data in movies:
        Movie.objects.get_or_create(
            title=movie_data["title"],
            defaults=movie_data,
        )

    # Create 20 seats shared across movie showings.
    for row in ["A", "B"]:
        for number in range(1, 11):
            Seat.objects.get_or_create(
                seat_number=f"{row}{number}",
                defaults={"is_booked": False},
            )


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_sample_data,
            migrations.RunPython.noop,
        ),
    ]
