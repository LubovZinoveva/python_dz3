# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_positions(list1):
    sum = 0
    for i in range(1, len(list1), 2):
        sum += list1[i]
    return sum

try:
    my_list = [2, 3, 5, 9, 3]
    my_sum = sum_odd_positions(my_list)
    print(f'Сумма = {my_sum}')
except:
    print('Ошибка')