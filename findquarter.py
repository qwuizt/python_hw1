x = float(input("Введите X: "))
y = float(input("Введите Y: "))
if x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print(" 3 четверть")
elif x > 0 and y < 0:
    print("4 четверть")
else:
    print("X and Y != 0")