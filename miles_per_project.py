def driving_cost(miles_per_gallon, gas_prices, how_many_miles):  
    your_value = how_many_miles / miles_per_gallon * gas_prices

    print(f"Your trip will cost you ${your_value:.2f}.")

driving_cost(20, 3.1599, 10)  # Expected output: Your trip will cost you 1.58.
driving_cost(20, 3.1599, 50)  # Expected output: Your trip will cost you 7.90.
driving_cost(20, 3.1599, 400)  # Expected output: Your trip will cost you 63.20.