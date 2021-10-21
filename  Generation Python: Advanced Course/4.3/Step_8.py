n = int(input())    # считываем значения n и m
my_list = []

for i in range(1, n+1):
    elem = [i for i in range(1, n+1)]
    my_list.append(elem)
for i in my_list:
    print(i)
