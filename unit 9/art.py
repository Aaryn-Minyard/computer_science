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

    def print_info(self):
        print(f'"{self.title}" was created by {self.artist.name} in {self.year_created}.')
        print(f'{self.artist.name} was born in {self.artist.birth_year} and died in {self.artist.death_year}.')

if __name__ == "__main__":
    user_artist_name = input("Enter artist name: ")
    user_birth_year = int(input("Enter birth year: "))
    user_death_year = int(input("Enter death year: "))
    user_title = input("Enter title of artwork: ")
    user_year_created = int(input("Enter year created: "))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()