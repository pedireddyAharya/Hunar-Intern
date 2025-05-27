import random
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
captcha = ''.join(random.choice(characters) for _ in range(5))
print("Generated Captcha:", captcha)
