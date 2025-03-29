def house_prices():
    while True: 
        current_price = int(input("House Price: "))
        old_price = int(input("Previous Listing: "))
        price_difference = current_price - old_price
        mortgage = (current_price * 0.051) / 12.
        print(f"This house is ${current_price}. The change is ${price_difference} since last month.")
        print(f"The estimated monthly mortgage is ${mortgage:.0f}.")
house_prices()