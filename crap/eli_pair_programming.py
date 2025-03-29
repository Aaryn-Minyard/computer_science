from artist import Artist
from artwork import Artwork

if __name__ == "__main__":
    user_artist_name = input("Enter artist name: ")
    user_birth_year = int(input("Enter birth year: "))
    user_death_year = int(input("Enter death year: "))
    user_title = input("Enter artwork title: ")
    user_year_created = int(input("Enter year created: "))
    type_of_art = input("Painting or Sculpture: ")

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist, art_type=type_of_art)
 
    new_artwork.print_info()