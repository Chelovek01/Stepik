number = input()
print(int(number[:-5] + number[-5:][::-1]))
