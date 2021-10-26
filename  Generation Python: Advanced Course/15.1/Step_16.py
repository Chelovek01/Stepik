def matrix(n=None, m=None, value=None):
    matrix1 = []

    if n is None:
        matrix1.append([0])

    elif n > 1 and m is None:
        for _ in range(n):
            matrix1.append(n * [0])

    elif n > 1 and m > 0 and value is None:
        for _ in range(n):
            matrix1.append(m * [0])

    elif n > 1 and m > 0 and value > 0:
        for _ in range(n):
            matrix1.append(m * [value])

    return matrix1
