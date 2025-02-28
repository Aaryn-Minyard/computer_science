import requests

def currency_converter():
    print("Welcome to the Currency Converter!")
    
    base_currency = input("Enter the base currency code (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency code (e.g., USD, EUR): ").upper()

    # Use try/except to safely convert user input into a number.
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount entered. Please enter a numeric value.")
        return

    # Build the API URL using the base currency.
    url = f"https://api.exchangerate.host/latest?base={base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        
        # Check if target currency is available in the response.
        rate = data["rates"].get(target_currency)
        if rate is None:
            print(f"Error: The target currency '{target_currency}' is not supported.")
            return
        
        converted_amount = amount * rate
        print(f"\n{amount:.2f} {base_currency} is equivalent to {converted_amount:.2f} {target_currency}")
        
    except requests.exceptions.RequestException as req_err:
        print("Network error occurred while fetching conversion rates:", req_err)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    currency_converter()
