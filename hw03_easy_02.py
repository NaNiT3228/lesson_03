# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def maximum_number(*args):
    list_args = list(args)
    max_value = list_args[0]
    for number in list_args:
        if int(max_value) < int(number):
            max_value = number
    return max_value




numbers = []

for i in range(3):
    numbers.append(input('Введите число: '))

max_number = maximum_number(*numbers)

print('Максимальное число из введенных:', max_number)