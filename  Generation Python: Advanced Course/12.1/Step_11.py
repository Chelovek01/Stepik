import random
num1 = random.randint(1, 2)

n = int(input())    # количество попыток
for i in range(n):
    num1 = num1
    if num1 == 1:
        print('Орел')
    else:
        print('Решка')
