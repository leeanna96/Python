import random

def genPass():
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789"
    password=""

    for i in range(6):
        index=random.randrange(len(alphabet))
        password+=alphabet[index]
    return password

print(genPass())
print(genPass())
print(genPass())
