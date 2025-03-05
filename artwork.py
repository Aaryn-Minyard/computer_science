import random
from artist import *

class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None, art_type="unknown"):
        # If no artist is provided, use the Artist default constructor
        if artist is None:
            artist = Artist()
        self.title = title
        self.year_created = year_created
        self.artist = artist
        self.type = art_type

    def price(self):
        # Check if we have valid birth and death years to avoid division by zero.
        # If either is -1 or the difference is 0, return an empty string (i.e. price not available)
        if self.artist.birth_year == -1 or self.artist.death_year == -1 or (self.artist.death_year - self.artist.birth_year) == 0:
            return ""
        
        # Calculate price based on type (convert type to lower case for safety)
        if self.type.lower() == 'painting':
            return self.painting_price()
        elif self.type.lower() == 'sculpture':
            return self.sculpture_price()
        else:
            return f"Unknown type of art: {self.type}"

    def painting_price(self):
        # Calculate a price based on the artwork's creation year relative to 2021
        if self.year_created < 2021:
            amount = 1000000 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
        elif self.year_created > 2021:
            amount = 12340.56 * (2021 + self.year_created) / (self.artist.death_year - self.artist.birth_year)
        else:
            amount = 12340.56 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
        return f"${amount:,.2f}"
        
    def sculpture_price(self):
        # Similar pricing logic can be applied for sculptures
        if self.year_created < 2021:
            amount = 2000000 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
        elif self.year_created > 2021:
            amount = 24540.56 * (2021 + self.year_created) / (self.artist.death_year - self.artist.birth_year)
        else:
            amount = 24540.56 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
        return f"${amount:,.2f}"

    def print_info(self):
        # First print the artist's information.
        self.artist.print_info()
        # Get the price string; if it’s empty, skip printing price and type.
        price_str = self.price()
        if price_str:
            print(f"Title: {self.title}, {self.year_created}, {price_str}, {self.type}")
        else:
            print(f"Title: {self.title}, {self.year_created}")