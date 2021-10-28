from functools import reduce

file = open('nums.txt', 'r')
languages = list(filter(lambda x: len(x) > 0, [line.strip() for line in file.readlines()]))
print(reduce(lambda x, y : int(x) + int(y), languages, 0))

file.close()
