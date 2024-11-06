from enum import Enum

class HighwayNumberError(ValueError):
    """Custom exception for invalid highway numbers."""
    pass

class HighwayDirection(Enum):
    NORTH_SOUTH = "North-South"
    EAST_WEST = "East-West"

class HighwayType(Enum):
    PRIMARY = "Primary"
    AUXILIARY = "Auxiliary"

class AmericanHighwayNumber:
    def __init__(self, number: int):
        # Validate before assignment
        AmericanHighwayNumber.validate_number(number)
        self.number = number

    @staticmethod
    def validate_number(number: int):
        if not isinstance(number, int):
            raise HighwayNumberError("Highway number must be an integer.")
        
        if number < 1 or number > 999:
            raise HighwayNumberError("Highway number must be between 1 and 999.")
        
        # Additional validation for auxiliary highway numbers
        if number >= 100:
            primary_number = number % 100
            if primary_number == 0:
                raise HighwayNumberError(
                    "Three-digit highway numbers must be auxiliary, meaning their last two digits cannot be zero."
                )

    @property
    def direction(self) -> HighwayDirection:
        """Return the highway's direction based on its number."""
        if self.number % 2 == 0:
            return HighwayDirection.EAST_WEST
        else:
            return HighwayDirection.NORTH_SOUTH

    @property
    def highway_type(self) -> HighwayType:
        """Return the highway's type (Primary or Auxiliary)."""
        if self.number < 100:
            return HighwayType.PRIMARY
        else:
            return HighwayType.AUXILIARY

    def __repr__(self):
        return f"AmericanHighwayNumber({self.number})"

# Example usage
try:
    # Prompt the user for input and convert it to an integer
    number = int(input("Enter a highway number (1-999): "))
    
    # Create an AmericanHighwayNumber object with the user input
    highway = AmericanHighwayNumber(number)
    print(f"Highway {highway.number} runs {highway.direction.value} and is a {highway.highway_type.value} highway.")
except HighwayNumberError as e:
    print(e)