def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Original price and discount percentage
original_price = 4500
discount_percent = 25

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if final_price != original_price:
    print("Final price after applying {}% discount: {:.2f}".format(discount_percent, final_price))
else:
    print("No discount applied, original price: {:.2f}".format(original_price))