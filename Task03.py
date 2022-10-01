# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def get_list(n):
    new_list = []
    for i in range(n):
        new_list.append(round(random.uniform(1.00, 10.00), 2))
    return new_list

def find_min(list1):
    min = 1.0
    for e in list1:
        if e - int(e) < min:
            min = round(e - int(e), 2)
    return min

def find_max(list2):
    max = 0.0
    for e in list2:
        if e - int(e) > max:
            max = round(e - int(e), 2)
    return max

try:
    number = int(input('Задайте размерность списка: '))
    my_list = get_list(number)
    my_min = find_min(my_list)
    my_max = find_max(my_list)
    print(my_list)
    print(f'min: {my_min}')
    print(f'max: {my_max}')
    print(f'max - min: {round(my_max - my_min, 2)}')
except:
    print('Ошибка, нужно ввести целое число')
