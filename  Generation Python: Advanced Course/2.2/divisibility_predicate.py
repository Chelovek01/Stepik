def func(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        False


num1, num2 = int(input()), int(input())


if func(num1, num2):
    True
    print('делится')
else:
    print('не делится')