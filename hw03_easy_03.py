# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_length_string(list_of_strings):
    return max(list(list_of_strings), key=len)


list_of_strings = []
while True:
    input_string = input('Введите строку символов(для прекращиения ввода - нажмите Enter: ')
    if input_string != '':
        list_of_strings.append(input_string)
    else:
        break

max_value = max_length_string(list_of_strings)
print('Максимальная по длине строка из введенных:', max_value)