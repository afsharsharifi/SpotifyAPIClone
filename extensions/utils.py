import random


def generate_otp(length=6):
    result = ""
    for i in range(length):
        result += str(random.randint(1, 9))
    return result
