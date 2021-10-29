with open("data.txt",encoding="UTF-8") as file:
    for i in file.readlines()[::-1]:
        print(i, end='')
