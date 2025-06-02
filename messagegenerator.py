# Greeting Message Generator
first_name = input("Enter your first name (max 10 characters): ")
last_name = input("Enter your last name (max 10 characters): ")


if len(first_name) > 10 or len(last_name) > 10:
    print("Names should not exceed 10 characters.")
else:
    print(f"Hello {first_name} {last_name}! You just developed into python.")
