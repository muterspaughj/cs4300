
Feature: Movie seat booking
  Users should be able to reserve available seats
  without allowing duplicate reservations.

  Scenario: Successfully book an available seat
    Given a movie and an available seat exist
    When a user books the available seat
    Then the booking should be created

  Scenario: Prevent duplicate bookings
    Given a movie seat is already booked
    When another user attempts to book the same seat
    Then the duplicate booking should be rejected

  Scenario: Allow the same seat for different movies
    Given two movies and an available seat exist
    When the seat is booked for both movies
    Then both bookings should be created
