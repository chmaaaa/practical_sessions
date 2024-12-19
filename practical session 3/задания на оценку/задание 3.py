# Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2, в противном случае уменьшить на 2.

a = input("Введите число: ")

# Обработка исключений

while type(a) != int:
    try:
        a = int(a)
        # Проверка, является ли число двухзначным
        if 10 <= abs(a) < 100:
            print("Вы ввели двухзначное число:", a)
        else:
            print("Число не является двухзначным!")
            a = input("Введите число: ")
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число: ")

b = a // 10 # Десятки (Первая цифра числа)
c = a % 10 # Единицы (Вторая цифра числа)

d = b+c

if d % 2 == 0:
    print ("Сумма цифр четная. Результат:", a + 2)
else:
    print ("Сумма цифр нечетная. Результат:", a - 2)