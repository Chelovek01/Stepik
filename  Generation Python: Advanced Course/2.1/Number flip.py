number = input()
list1 = []
list2 = list1[-5:]
list3 = list2.reverse()
print(list3)
for i in number:
    list1 += i
print(list1)
if len(list1) > 5:
    print(''.join(list1[0:1]), ''.join(list2.reverse()))
else:
    False
