'''
This Program is created to suggest the strong password for better security .
This program import "random" inbult python function to generate password .
'''

import random
from string import digits, punctuation, ascii_letters

length = 20
symbol = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbol) for _ in range(length))

print(password)