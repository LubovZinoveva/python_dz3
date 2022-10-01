# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def get_binary(number):
    binary_num = []
    while number > 0:
        binary_num.append(number % 2)
        number //= 2
    result = binary_num[-1]
    for i in range(-2, -len(binary_num) - 1, -1):
        result = result * 10 + binary_num[i]
    return result

try:
    num = int(input('Десятичное число = '))
    bin_num = get_binary(num)
    print(f'Двоичное число = {bin_num}')
except:
    print('Ошибка, введите целое число')