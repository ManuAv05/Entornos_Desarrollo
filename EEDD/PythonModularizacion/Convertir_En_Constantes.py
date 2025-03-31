

def calculate_price():
    PRICE=100
    discounted_price = PRICE - (PRICE * 0.15)
    final_price = discounted_price + (discounted_price * 0.21)
    print(f"Final price: {final_price}")

calculate_price()