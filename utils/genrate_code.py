import random


def genrate_code(length=8):
    numbers = '0123456789'
    code = ''.join(random.choice(numbers) for x in range(length))
    return code

# print(genrate_code())