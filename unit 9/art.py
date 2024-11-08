tier1 = ["Leonardo da Vinci","Vincent van Gogh","Pablo Picasso","Michelangelo", "Rembrandt"
]

tier2 = ["Claude Monet","Salvador Dalí","Frida Kahlo","Georgia O'Keeffe","Andy Warhol"
]

tier3 = ["Gustav Klimt","Edvard Munch","Wassily Kandinsky","René Magritte","Hieronymus Bosch"
]

class Artist:
   def __init__(self, name, birth_year, death_year):
       self.name = name
       self.birth_year = birth_year
       self.death_year = death_year
       print(f'{self.name}, {self.birth_year} - {self.death_year}')

      
class Artwork:
    def __init__(self, title, year_created, artist):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def price(self):
        amount = 12340.56 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year) # default value
         
        if self.artist.name in tier1:
            amount = 5000000 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
            return f"${amount:,.2f}"
        elif self.artist.name in tier2:
            amount = 1000000 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
            return f"${amount:,.2f}"
        elif self.artist.name in tier3:
            amount = 400000 * (2021 - self.year_created) / (self.artist.death_year - self.artist.birth_year)
            return f"${amount:,.2f}"
        elif self.year_created > 2021:
            amount = 12340.56 * (2021 + self.year_created) / (self.artist.death_year - self.artist.birth_year)
            return f"${amount:,.2f}"
        else:
            return f"${amount:,.2f}"

    def print_info(self):
        print(f'"{self.title}" was created by {self.artist.name} in {self.year_created}.')
        print(f'{self.artist.name} was born in {self.artist.birth_year} and died in {self.artist.death_year}.')
        print(f'This artwork is worth {self.price()}')

if __name__ == "__main__":
    user_artist_name = input("Enter artist name: ")
    user_birth_year = int(input("Enter birth year: "))
    user_death_year = int(input("Enter death year: "))
    user_title = input("Enter title of artwork: ")
    user_year_created = int(input("Enter year created: "))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()