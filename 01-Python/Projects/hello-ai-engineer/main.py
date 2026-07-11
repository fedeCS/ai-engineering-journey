APP_NAME = "AI Engineer Journey"
VERSION = "1.0.0"

def print_banner():
    print("=" * 50)
    print(f"{APP_NAME}")
    print(f"Version: {VERSION}")
    print("=" * 50)

def welcome_user():
    print("Welcome!")
    print("My name is Federico.")
    print("Today I officially start my AI Engineering journey.")
    print("This repository will grow as I learn")
    print("Today's goals")
    print("✓ Learn Python")
    print("✓ Build Projects")
    print("✓ Learn AI")
    print("✓ Never Stop Learning")

def print_quote():
    print("“The best way to predict the future is to invent it.” – Alan Kay")   





def main():
    print_banner()
    welcome_user()
    print_quote()


if __name__ == "__main__":
    main()