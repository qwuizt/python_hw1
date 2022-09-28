day  = int(input("Введите день недели: "))
if day > 0 and day < 6:
    print("будний")
elif day > 5 and day < 8:
    print("выходной")
else:
     print("Число не является днем недели")  