# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

c = a + b # Ввод новой переменной (сумма чисел)

if c % 5 == 0:
    print("Сумма чисел кратна 5. Результат:", c + 1)
else:
    print("Сумма чисел не кратна 5. Результат:", c - 2)