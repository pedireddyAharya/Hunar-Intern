import random

# Define all possible characters: uppercase, lowercase, digits
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

# Generate captcha by picking 5 random characters
captcha = ''.join(random.choice(characters) for _ in range(5))

# Print the generated captcha
print("Generated Captcha:", captcha)
