APP_NAME="🤖 AI Engineer Terminal Assistant"

def print_banner():
    print("=" * 50)
    print(f"{APP_NAME}")
    print("=" * 50)

def get_banner():
    name = input("Enter your name: ")
    dream_job = input("Enter your dream job: ")
    favorite_language = input("Enter your favorite programming language: ")
    return name, dream_job, favorite_language


def greet_user(name, dream_job, favorite_language):
    print(f"\nWelcome, {name}!")
    print(f"Your dream job is {dream_job}.")
    print(f"Your favorite programming language is {favorite_language}.")
    print("Let's start your AI Engineering journey.")

def main():
    print_banner()
    name, dream_job, favorite_language = get_banner()
    greet_user(name, dream_job, favorite_language)

if __name__ == "__main__":
    main()