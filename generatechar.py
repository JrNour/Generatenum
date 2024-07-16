import string
from itertools import product

with open('6char.txt', 'w') as file:
    for letters in product(string.ascii_lowercase, repeat=6):
        file.write(''.join(letters) + '\n')
