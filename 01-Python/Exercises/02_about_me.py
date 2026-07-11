name = "Federico"
age = 32
country = "USA"
language = "Python"
current_goal = "Become an AI Engineer and build production AI systems."



def print_banner():
    print("=" * 50)
    print("🤖 AI ENGINEER PROFILE")
    print("=" * 50)

def print_profile():
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print(f"Favorite Language: {language}")

def print_current_goal():
    print(f"Current Goal: {current_goal}")

def main():
    print_banner()
    print_profile()
    print_current_goal()

if __name__ == "__main__":
    main()