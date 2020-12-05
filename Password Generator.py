import string
import random

def generatePassword(length):
    chars = string.ascii_letters + string.digits
    password = "".join(random.sample(chars, length))
    return password

password = generatePassword(12)
print(password)