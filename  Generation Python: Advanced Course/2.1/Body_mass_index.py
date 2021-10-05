mass = float(input())
light = float(input())
bmi = mass / (light * light)
if 18 <= bmi <= 25:
    print("Оптимальная масса")
elif bmi < 18.5:
    print("Недостаточная масса")
elif bmi > 25:
    print("Избыточная масса")