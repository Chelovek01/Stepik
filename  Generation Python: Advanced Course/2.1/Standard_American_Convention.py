digit = input()[::-1]
result = []
n = 3
for i in range(0, len(digit), n):
    result.extend(digit[i : i+n])
    result.append(',')
result.pop()

print(''.join(result[::-1]))

