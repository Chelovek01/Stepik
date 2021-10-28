file = open(input(), 'r')
language = file.readlines()
print(language[-2])

file.close()