
APP_NAME="🤖 AI Engineer Terminal Assistant"

def print_banner():
    print("=" * 50)
    print(f"{APP_NAME}")
    print("=" * 50)

def get_user_info():
    name = input("Enter your name: ")
    dream_job = input("Enter your dream job: ")
    favorite_language = input("Enter your favorite programming language: ")
    return name, dream_job, favorite_language


def greet_user(name, dream_job, favorite_language):  # noqa: F811
    print("\n===== Profile =====")
    print(f"Name: {name}")
    print(f"Dream Job: {dream_job}")
    print(f"Favorite Language: {favorite_language}")

def main():
    print_banner()
    name, dream_job, favorite_language = get_user_info()  # noqa: F811
    greet_user(name, dream_job, favorite_language)

if __name__ == "__main__":
    main()