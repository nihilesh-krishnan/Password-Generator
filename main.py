import random
import string

def generate_password(length):
    letters=string.ascii_letters
    digits = string.digits
    symbols = string.digits
    all_chars = letters #if wanted can add symbols and digits by simply (+ digits; + symbols)


    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

password = generate_password(6) #can change the password length

print(password)