from functools import reduce

file = open('numbers.txt', 'r')
print(reduce(lambda x, y : int(x) + int(y), file.readlines(), 0))

file.close()