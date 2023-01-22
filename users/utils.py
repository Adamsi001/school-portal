import random
import string


USER_ID_MIN_LENGTH = 11


def generateUserID():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters)
                            for i in range(USER_ID_MIN_LENGTH))

    return random_string
