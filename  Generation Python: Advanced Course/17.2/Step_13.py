import random

file = open('lines.txt', 'r')
language = file.readlines()
print(random.choice(language))

file.close()
