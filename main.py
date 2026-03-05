import random
import math

def task1():
    numbers = [random.randint(0, 100) for _ in range(20)]
    print("Згенеровані числа:", numbers)
    result = [n for n in numbers if n <= 50]
    print("Числа з першої половини інтервалу (0–50):", result)

def task2():
    s = float(input("Введіть суму покупки: "))
    if s > 1000:
        s *= 0.95
    elif s > 500:
        s *= 0.97
    print("Сума з урахуванням знижки:", s)

def task3():
    a = float(input("Введіть довжину основи: "))
    h = float(input("Введіть висоту: "))
    area = (a * h) / 2
    print("Площа трикутника:", area)
    if area % 2 == 0:
        print("Площа парна. Результат ділення на 2:", area / 2)
    else:
        print("Не можу ділити на 2!")

def task4():
    A = int(input("A: "))
    B = int(input("B: "))
    while A >= B:
        print("A має бути менше за B. Спробуйте ще раз.")
        A = int(input("A: "))
        B = int(input("B: "))
    total = 0
    for i in range(A, B + 1):
        total += i
    print("Сума:", total)

def task5():
    A = int(input("A: "))
    B = int(input("B: "))
    while A >= B:
        print("A має бути менше за B. Спробуйте ще раз.")
        A = int(input("A: "))
        B = int(input("B: "))
    total = 0
    for i in range(A, B + 1):
        total += i * i
    print("Сума квадратів:", total)

def task6():
    a = int(input("a: "))
    b = int(input("b: "))
    total = 0
    while a >= b:
        print("A має бути менше B. Спробуйте ще раз.")
        a = int(input("a: "))
        b = int(input("b: "))
    while a <= b:
        total += a
        a += 1
    print("Сума:", total)

def task7():
    a = int(input("a (0–50): "))
    while a > 50 or a < 0:
        print("A має бути від 0-50. Спробуйте ще раз.")
        a = int(input("a: "))
    total = 0
    for i in range(a, 51):
        total += i * i
    print("Сума квадратів:", total)

def task8():
    N = int(input("N (>1): "))
    while N < 1:
        print("N має бути більше 1. Спробуйте ще раз.")
        N = int(input("N (>1): "))
    K = 1
    while 5 ** K <= N:
        K += 1
    print("Найменше K:", K)

def task9():
    n = int(input("n: "))
    for i in range(1, 10000):
        sq = i * i
        if sq > n:
            print("Перше число більше n:", sq)
            break

def task10():
    n = int(input("n: "))
    x = 0
    add = 0
    while add <= n:
        add = x * x + 1
        x += 1
    print("Перше число більше n:", add)

def task11():
    D = int(input("День: "))
    while D < 1 or D>31:
        print("Такий день місяця неможливий")
        D = int(input("День: "))
    M = int(input("Місяць: "))
    while M < 1 or M>12:
        print("Такий місяць неможливий")
        M = int(input("Місяць: "))

    if (D >= 20 and M == 1) or (D <= 18 and M == 2):
        print("Водолій")
    elif (D >= 19 and M == 2) or (D <= 20 and M == 3):
        print("Риби")
    elif (D >= 21 and M == 3) or (D <= 19 and M == 4):
        print("Овен")
    elif (D >= 20 and M == 4) or (D <= 20 and M == 5):
        print("Телець")
    elif (D >= 21 and M == 5) or (D <= 21 and M == 6):
        print("Близнюки")
    elif (D >= 22 and M == 6) or (D <= 22 and M == 7):
        print("Рак")
    elif (D >= 23 and M == 7) or (D <= 22 and M == 8):
        print("Лев")
    elif (D >= 23 and M == 8) or (D <= 22 and M == 9):
        print("Діва")
    elif (D >= 23 and M == 9) or (D <= 22 and M == 10):
        print("Терези")
    elif (D >= 23 and M == 10) or (D <= 22 and M == 11):
        print("Скорпіон")
    elif (D >= 23 and M == 11) or (D <= 21 and M == 12):
        print("Стрілець")
    else:
        print("Козеріг")

def task12():
    print("1 — кг, 2 — мг, 3 — г, 4 — т, 5 — центнер")
    t = int(input("Оберіть одиницю: "))
    m = float(input("Введіть масу: "))

    if t == 1:
        kg = m
    elif t == 2:
        kg = m / 1_000_000
    elif t == 3:
        kg = m / 1000
    elif t == 4:
        kg = m * 1000
    elif t == 5:
        kg = m * 100
    else:
        print("Невірний вибір!")
        return

    print("Маса у кілограмах:", kg)


while True:
    print("\n=== МЕНЮ ЗАВДАНЬ ===")
    print("1–12 — виберіть завдання")
    print("0 — вихід")

    choice = input("Ваш вибір: ")

    if choice == "1": task1()
    elif choice == "2": task2()
    elif choice == "3": task3()
    elif choice == "4": task4()
    elif choice == "5": task5()
    elif choice == "6": task6()
    elif choice == "7": task7()
    elif choice == "8": task8()
    elif choice == "9": task9()
    elif choice == "10": task10()
    elif choice == "11": task11()
    elif choice == "12": task12()
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір!")
