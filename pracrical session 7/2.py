# Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Преобразовать каждое слово в
# строке, заменив в нем все предыдущие вхождения его последней буквы на символ
# «.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ».
# Количество пробелов между словами не изменять.

# Вводим строку
line = input("Введите строку из русских слов, набранных с CapsLock: ")

# Разделяем строку на слова
words = line.split()

# Создаем список для преобразованных слов
new_words = []

# Обрабатываем каждое слово
for word in words:
    last_char = word[-1]  # Находим последнюю букву
    new_word = ""  # Строка для нового слова
    for i in range(len(word)):  # Идем по каждой букве
        if word[i] == last_char and i != len(word) - 1:  # Если это не последняя буква, заменяем на точку
            new_word += "."
        else:
            new_word += word[i]  # Иначе добавляем букву как есть
    new_words.append(new_word)  # Добавляем преобразованное слово в список

# Соединяем слова обратно в строку
result_string = " ".join(new_words)

print("Результат:", result_string)