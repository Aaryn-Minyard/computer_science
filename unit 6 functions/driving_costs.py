# Define your function here
def main(miles_per_gallon, dollars_per_gallon, miles_driven):
    # Calculate the cost of driving based on inputs
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    # Input the car's miles per gallon and the price of gas
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    
    
    # Output the cost for driving 10 miles, 50 miles, and 400 miles
    cost_10_miles = main(miles_per_gallon, dollars_per_gallon, 10.0)
    cost_50_miles = main(miles_per_gallon, dollars_per_gallon, 50.0)
    cost_400_miles = main(miles_per_gallon, dollars_per_gallon, 400.0)
    
    # Print the results with 2 decimal points
    print(f'{cost_10_miles:.2f}')
    print(f'{cost_50_miles:.2f}')
    print(f'{cost_400_miles:.2f}')

