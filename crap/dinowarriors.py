import wikipediaapi
import random


wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='MyDinosaurApp/1.0 (https://example.com; contact@example.com)'
)

def load_dinosaur_list(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_random_dinosaur(dinosaur_list):
    if dinosaur_list:
        return random.choice(dinosaur_list)
    else:
        return "No dinosaurs available."


dinosaur_list = load_dinosaur_list('dinosaurs.txt')


def get_dinosaur_info(dinosaur_name):
    page = wiki_wiki.page(dinosaur_name)
    if page.exists():
        return page.summary[:500]  
    else:
        return f"Sorry, no information found for '{dinosaur_name}'."


def get_random_dinosaur_info():
    random_dino = get_random_dinosaur(dinosaur_list)
    return f"Random Dinosaur: {random_dino}\n{get_dinosaur_info(random_dino)}"


def display_menu():
    while True:
        print("\nDinosaur Information Menu")
        print("1. Get information about a specific dinosaur")
        print("2. Get information about a random dinosaur")
        print("3. Exit")
        
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            dino_name = input("Enter the name of a dinosaur: ")
            print(get_dinosaur_info(dino_name))
        elif choice == '2':
            print(get_random_dinosaur_info())
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


display_menu()
