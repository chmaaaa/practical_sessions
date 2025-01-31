# Дано целое число N (> 0). Найти сумму 1^N + 2^(N-1) + ... + N^1.

# Ввод целого числа N (> 0)
n = input("Введите целое число N (> 0): ")

# Обработка исключений для N: проверка, что N - целое и > 0. 
while True:
    try:
        n = int(n)  # Преобразование в тип int
        if n > 0:  # Проверка, что число больше 0
            break  # Выход из цикла в случае отсутствия проблем
        else:
            print("Число N должно быть больше 0.")  # Если число < = 0, вывод сообщения
    except ValueError:  # Ошибка в случае некорректного ввода
        print("Ошибка! Введите целое число.")  # Сообщение об ошибке
    n = input("Введите целое число N (> 0): ")  # Повторный ввод

# Переменная для хранения результата суммы
result = 0

# Цикл для вычисления суммы ряда. В цикле перебор значений от 1 до N включительно..
for i in range(1, n + 1):
    power = n - i + 1  # Степень для текущего числа i (формула: N - i + 1)
    result += i ** power  # Вычисление i в степени (N - i + 1) и добавление к сумме

# Вывод результата
print(f"Сумма ряда = {result}")