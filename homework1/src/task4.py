# Calculate the final price after applying a discount
def calculate_discount(price, discount):

    # Check that price and discount are numeric values
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("Price and discount must be numeric")

    # Check that the price is not negative
    if price < 0:
        raise ValueError("Price cannot be negative")

    # Check that the discount is between 0 and 100
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")

    # Calculate the amount being discounted
    discount_amount = price * (discount / 100)

    # Calculate and return the final price
    return price - discount_amount