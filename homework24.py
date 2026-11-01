
import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits

password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(numbers)
]

characters = uppercase + lowercase + numbers

for i in range(5):
    password.append(random.choice(characters))

random.shuffle(password)

password = "".join(password)

print("Random Password:", password)
