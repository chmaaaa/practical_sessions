# Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих»

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    # Проверка наличия хотя бы одной пары совпадающих чисел
    if a == b or a == c or b == c: 
        print("Среди трёх данных чисел есть хотя бы одна пара совпадающих: ", True)
    else:
        print("Среди трёх данных чисел нет ни одной пары совпадающих: ", False)

except ValueError:
    print("Пожалуйста, введите целое число!") # обработка исключений 