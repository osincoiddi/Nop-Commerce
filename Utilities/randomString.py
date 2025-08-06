import random
import string
from random import choice
from string import ascii_lowercase

def random_String_generator(size=5, chars=ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))