


APP_NAME="🤖 AI Engineer Terminal Assistant"

def print_banner():
    print("=" * 50)
    print(f"{APP_NAME}")
    print("=" * 50)

def show_menu():
    print("\nChoose an option:")
    print("1. About Me")
    print("2. Favorite Language")
    print("3. Favorite Game")
    print("4. Favorite Food")
    print("5. Dream Company")
    print("6. Exit")

PROFILE = {
    "name": "Federico",
    "favorite_language": "Python",
    "country": "Las Vegas",
    "favorite_game": "Wind Whacker",
    "favorite_movie": "the Matrix",
    "favorite_food": "ass",
    "dream_company": "Google"
}

def about_me():
    print(f"\nMy name is {PROFILE['name']} im from {PROFILE['country']}.")

def favorite_language():
    print(PROFILE['favorite_language'])

def favorite_game():
    print(PROFILE['favorite_game'])

def favorite_food():
    print(PROFILE['favorite_food'])

def dream_company():
    print(PROFILE['dream_company'])


def main():
    print_banner()
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            about_me()
        elif choice == '2':
            favorite_language()
        elif choice == '3':
            favorite_game()
        elif choice == '4':
            favorite_food()
        elif choice == '5':
            dream_company()
        elif choice == '6':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
