# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д. Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

def get_list(n):
    new_list = []
    for i in range(n):
        new_list.append(randint(1, 10))
    return new_list

def multiplication_pair(numbers):
    count = -1
    result =[]
    for i in range(len(numbers)//2):
        result.append(numbers[i]*numbers[count])
        count -= 1
    if len(numbers) % 2 != 0:
        result.append(numbers[len(numbers)//2]**2)
    return result

try:
    num = int(input('Задайте размерность списка: '))
    my_list = get_list(num)
    multi = multiplication_pair(my_list)
    print(my_list)
    print(multi)
except: 
    print('Ошибка, нужно ввести целое число')