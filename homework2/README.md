# CinemaBooking — Movie Theater Booking System

**CS 4300 — Software Engineering**  
**Homework 2**

## Project Overview

CinemaBooking is a web-based movie theater booking application built using Django, Django REST Framework, SQLite, PostgreSQL, and Bootstrap.

The application allows users to browse available movies, create an account, log in, reserve theater seats, and view their booking history. It also provides REST API endpoints for managing movies, seats, and bookings.

The project demonstrates full-stack web development, database modeling, authentication, REST API development, automated testing, and cloud deployment.

**Live Website:** https://cinemabooking-9u01.onrender.com

## Features

- **Movie Listings:** Browse movies with descriptions, release dates, and durations.
- **User Registration:** Create an account using Django's built-in authentication system.
- **User Authentication:** Log in and log out securely.
- **Seat Reservations:** Select and reserve available theater seats.
- **Double-Booking Prevention:** Prevent the same seat from being reserved twice for the same movie.
- **Booking History:** View previous reservations associated with the logged-in user.
- **REST API:** Access movies, seats, and bookings through Django REST Framework.
- **Responsive Interface:** Bootstrap-based pages that work on desktop and mobile devices.
- **Database Integration:** SQLite for local development and PostgreSQL for production deployment.
- **Cloud Deployment:** Hosted using Render.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web application framework |
| Django REST Framework | REST API development |
| SQLite | Local development database |
| PostgreSQL | Production database |
| Bootstrap | Responsive frontend styling |
| HTML/CSS | Website structure and styling |
| Gunicorn | Production application server |
| WhiteNoise | Static file serving |
| Render | Cloud hosting |
| Git/GitHub | Version control |
| Django Test Framework | Unit and integration testing |
| Behave | Behavior-driven testing |
| Coverage.py | Test coverage measurement |

## Project Structure

```text
homework2/
├── .venv/
├── requirements.txt
├── README.md
└── movie_theater_booking/
    ├── manage.py
    ├── build.sh
    ├── movie_theater_booking/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── bookings/
        ├── migrations/
        ├── templates/
        │   ├── bookings/
        │   │   ├── base.html
        │   │   ├── movie_list.html
        │   │   ├── seat_booking.html
        │   │   └── booking_history.html
        │   └── registration/
        │       ├── login.html
        │       └── signup.html
        ├── models.py
        ├── views.py
        ├── serializers.py
        ├── urls.py
        ├── admin.py
        └── tests.py
```

## Database Models

### Movie

Stores information about available movies.

- `title` — Movie title
- `description` — Movie description
- `release_date` — Original release date
- `duration` — Movie duration in minutes

### Seat

Represents a seat in the movie theater.

- `seat_number` — Unique seat identifier
- `is_booked` — Seat booking status field

### Booking

Stores reservations made by registered users.

- `movie` — Foreign key to Movie
- `seat` — Foreign key to Seat
- `user` — Foreign key to Django's User model
- `booking_date` — Date and time of the reservation

A database uniqueness constraint prevents multiple bookings for the same movie and seat combination.

Seat availability is determined using existing bookings for each movie.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/muterspaughj/cs4300.git
cd cs4300/homework2
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r movie_theater_booking/requirements.txt
```

### 4. Navigate to the Django project

```bash
cd movie_theater_booking
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## Using the Application

### Creating an Account

1. Navigate to the signup page.
2. Enter a username and password.
3. Confirm the password.
4. Submit the registration form.
5. Log in using the new account.

Signup URL: `/accounts/signup/`

### Booking a Seat

1. Log in to CinemaBooking.
2. Browse the available movies.
3. Select a movie.
4. View the available seats.
5. Choose an available seat and confirm the booking.
6. View the reservation in Booking History.

Users cannot reserve a seat that has already been booked for the same movie.

### Viewing Booking History

Authenticated users can view their reservations at:

`/history/`

Each reservation is associated with the user who created it.

## REST API Endpoints

The application uses Django REST Framework.

| Endpoint | Description |
|---|---|
| `/api/movies/` | List and manage movies |
| `/api/seats/` | List and manage seats |
| `/api/bookings/` | Access bookings associated with the authenticated user |
| `/api-auth/` | Django REST Framework authentication interface |

The API uses ModelViewSets and serializers to manage database records.

Booking API operations require authentication. Booking updates are restricted to preserve reservation integrity.

## Testing

The project includes automated Django tests and behavior-driven tests.

### Run Django Tests

From the directory containing `manage.py`:

```bash
python manage.py test
```

The project was tested with 14 passing Django tests.

### Run Behavior-Driven Tests

```bash
python manage.py behave
```

The BDD test suite was tested with 3 passing scenarios and 9 passing steps.

### Run Coverage Analysis

```bash
coverage run manage.py test
coverage report -m
```

The recorded test coverage was **87%**, exceeding the 80% coverage target.

Coverage results may change as additional code is added.

## Deployment

CinemaBooking is deployed using Render.

**Live Application:** https://cinemabooking-9u01.onrender.com

The deployment uses:

- Gunicorn to serve Django.
- WhiteNoise to serve static files.
- PostgreSQL for production data storage.
- Environment variables for production configuration.
- A build script for dependency installation, static file collection, and database migrations.

### Render Configuration

**Root Directory:**

```text
homework2/movie_theater_booking
```

**Build Command:**

```bash
./build.sh
```

**Start Command:**

```bash
gunicorn movie_theater_booking.wsgi:application
```

### Environment Variables

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Django application secret |
| `DEBUG` | Enables or disables debug mode |
| `ALLOWED_HOSTS` | Configures accepted hostnames |
| `CSRF_TRUSTED_ORIGINS` | Configures trusted request origins |
| `DATABASE_URL` | PostgreSQL database connection |

Production secrets and database credentials should not be committed to GitHub.

## Security Features

The application includes several security mechanisms:

- Django's built-in password hashing and authentication.
- Login requirements for seat booking and booking history.
- CSRF protection for HTML forms.
- Database constraints to prevent duplicate seat reservations.
- Atomic database transactions for booking creation.
- User-specific booking queries.
- Restrictions on modifying existing bookings through the API.
- Environment-based production settings.

## AI Usage Disclosure

AI assistance was used during the development of this project for:

- Explaining Django project structure and configuration.
- Assisting with database models and REST API implementation.
- Developing and refining Bootstrap templates.
- Implementing user authentication and registration.
- Troubleshooting Python virtual environments and dependency errors.
- Debugging GitHub and Render deployment issues.
- Assisting with test development and coverage analysis.
- Generating documentation and README content.

AI-generated suggestions were reviewed, integrated, and tested during development. GitHub was used to track project changes.

## Future Improvements

Potential improvements include:

- Movie posters and additional movie details.
- Showtime selection and scheduling.
- Multiple theater rooms.
- Interactive seat maps.
- Email booking confirmations.
- Reservation cancellation.
- Payment processing.
- Additional API permissions and security controls.
- Expanded automated testing.

## Conclusion

CinemaBooking demonstrates the development of a full-stack movie theater reservation system using Django and Django REST Framework.

The project integrates relational database models, user authentication, seat reservation logic, REST API endpoints, automated testing, and cloud deployment into a functional web application.