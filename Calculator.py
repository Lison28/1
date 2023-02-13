print("Здравствуйте! Введите количество операций, которые хотите осуществить:")
count = int(input())
print("Введите первое число:")
first = float(input())
res = first
for i in range(count):
    print("Введите следующее число:")
    second = int(input())
    print("Введите номер операции:\n1) +\n2) -\n3) *\n4) /\n5) Возведение в степень(второе введенное число будет считаться степенью)")
    operation = int(input())
    if operation == 1:
        res += second
        print(f"Результат: {res}")
        i -= 1
    elif operation == 2:
        res -= second
        print(f"Результат: {res}")
        i -= 1
    elif operation == 3:
        res *= second
        print(f"Результат: {res}")
        i -= 1
    elif operation == 4:
        if second == 0:
            print("На ноль делить нельзя!")
            i += 1
            continue
        res = float(res / second)
        print(f"Результат: {res}")
        i -= 1
    elif operation == 5:
        j = 1
        st = res
        while j in range(second):
            res *= st
            j += 1
        print(f"Результат: {res}")
        i -= 1
    else:
        print("Выбрано несуществующее число!")