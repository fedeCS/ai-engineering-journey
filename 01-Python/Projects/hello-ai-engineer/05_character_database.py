characters = [
    {
        "name": "Federico",
        "class": "Guildmaster",
        "level": 99,
        "health": 5000
    },
    {
        "name": "Arthas",
        "class": "Paladin",
        "level": 80,
        "health": 3500
    },
    {
        "name": "Jaina",
        "class": "Mage",
        "level": 82,
        "health": 2200
    }
]
def print_banner():
    print("="*40 + "Guild Roster" + "="*40)

def display_characters():
    for character in characters: 

        print("="*30)
        print(f"Name: {character['name']}")
        print(f"Class: {character['class']}")
        print(f"Level: {character['level']}")
        print(f"Health: {character['health']}")

def recruit_character():
    name = input("Enter the character's name: ")
    char_class = input("Enter the character's class: ")
    level = int(input("Enter the character's level: "))
    health = int(input("Enter the character's health: "))

    new_character = {
        "name": name,
        "class": char_class,
        "level": level,
        "health": health
    }

    characters.append(new_character)
    print(f"{name} has been recruited to the guild!")        

def show_menu():
    print_banner()
    print("1. Display Characters")
    print("2. Recruit Character")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3 ): ")
        
        if choice == '1':
            display_characters()
        elif choice == '2':
            recruit_character()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
