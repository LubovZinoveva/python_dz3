# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры),
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился
# на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре,
# то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random

def get_list(row, column):
    numbers = []
    for i in range(row):
        numbers.append([random.randint(10, 90) for _ in range(column)])
    return numbers

def print_list(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end=' ')
        print()

def mix_list(array, row1, column1):
    new_list = []
    result_list = []
    result = []
    len2 = len(array)//2

    for i in range(len(array)):
        for j in range(len(array[i])):
            new_list.append(array[i][j])

    for i in range(len(new_list)//2):
        if i < 3:
            index1 = random.randint(len2, len(new_list) - 1)
            result_list.append(new_list[index1])
            new_list.pop(index1)
            index2 = random.randint(len2, len(new_list) - 1)
            result_list.append(new_list[index2])
            new_list.pop(index2)
        else:
            index1 = random.randint(0, len(new_list) - 1)
            result_list.append(new_list[index1])
            new_list.pop(index1)
            index2 = random.randint(0, len(new_list) - 1)
            result_list.append(new_list[index2])
            new_list.pop(index2)
    
    index = 0    
    for l in range(row1):
            result.append([])
            for m in range(column1):
                result[l].append(result_list[index])
                index += 1
    return result
    

m = int(input('Количество строк = '))
n = int(input('Количество столбцов = '))
if m*n % 2 != 0:
    print('Элементов нечетное количество')
else:
    my_list = get_list(m, n)
    print_list(my_list)
    print()
    my_list = mix_list(my_list, m, n)
    print_list(my_list)
