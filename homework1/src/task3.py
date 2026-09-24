# Check if a number is positive, negative, or zero
def check_number(number):

    # Check if the number is greater than zero
    if number > 0:
        return "positive"

    # Check if the number is less than zero
    elif number < 0:
        return "negative"

    # The number must be zero if neither condition is true
    else:
        return "zero"


# Create an empty list to store the first 10 prime numbers
prime_numbers = []

# Start checking numbers at 2
number = 2

# Continue until 10 prime numbers have been found
for number in range(2, 100):

    # Assume the number is prime
    is_prime = True

    # Check if the number can be divided evenly by any smaller number
    for divisor in range(2, number):

        # The number is not prime if there is no remainder
        if number % divisor == 0:
            is_prime = False
            break

    # Add the number to the list if it is prime
    if is_prime:
        prime_numbers.append(number)

    # Stop once the first 10 prime numbers have been found
    if len(prime_numbers) == 10:
        break

    # Print the first 10 prime numbers
    print(prime_numbers)


# Start the sum at zero
total = 0

# Start counting at 1
number = 1

# Continue while the number is 100 or less
while number <= 100:

    # Add the current number to the total
    total += number

    # Move to the next number
    number += 1