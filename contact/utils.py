import random
import string


def genereate_code():
    verification_code = ""
    list1 = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    for _ in range(5):
        verification_code += random.choice(list1)
    return verification_code
