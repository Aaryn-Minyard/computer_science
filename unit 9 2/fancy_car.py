FULL_TANK = 14

class FancyCar:
    def __init__(self, make="Old Clunker", model="classic", odometer=123000 ,mpg=24.0):
        # Complete the constructor.
        self.make = ""
        self.model = ""
        self.odometer = ""
        self.mpg = ""
        

    # Return car model
    def get_model(self):
        # Update the return statment.
        model = self.model
        
        
        return f"the model is {model}"

    # Return car odometer
    def check_odometer(self):
        # Update the return statment.
        
        return 0

    # Return miles per gallon (MPG)
    def get_mpg(self):
        # Update the return statment.
        
        return 0.0

    # Return amount of gas in tank
    def check_gas_gauge(self):
        # Update the return statment.
        
        return 0.0

    # Honk horn
    def honk_horn(self):
        # Type your code here.
        print('')

    # Drive car requested miles but check for enough,
    # checking that miles_to_drive is positive
    def drive(self, miles_to_drive):
        # Type your code here and remove the return statement
        
        return -1

    # Add gas to tank. Check for positive value of amount to add
    def add_gas(self, amount_to_add):
        # Type your code here and remove the return statement
        
        return -1

    # Set boolean variable to True
    def start_engine(self):
        # Type your code here and remove the return statement
        
        return -1

    # Set boolean variable to False
    def stop_engine(self):
        # Type your code here and remove the return statement
        
        return -1

if __name__ == '__main__':
    my_car = FancyCar()

    # Just for initial testing
    print(f"make={my_car.get_model()}")
    print(f"mpg={my_car.get_mpg()}")
    print(f"odometer={my_car.check_odometer()}")
    print(f"gas_tank={my_car.check_gas_gauge()}")