# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def input_num(mesage: str) -> int:
    while True:
        num = input(mesage)
        if num.isdigit():
            return int(num)

def min_position(my_list, num_min) -> int:
    for i in range(len(my_list)):
        if my_list[i] >= num_min :
            return i

def max_position(my_list, num_max) -> int:
    for i in range(len(my_list)):
        if my_list[i] > num_max:
            return i


my_list = sorted(randint(0,100) for _ in range(20))

print(my_list)

first_num = input_num('Введите первое число(цифру): ')
second_num = input_num('Введите второе число(цифру): ')

min_index = min_position(my_list,first_num)
max_index = max_position(my_list,second_num)

print(f'в диапазоне от {first_num} до {second_num} лежит: {my_list[min_index:max_index]}')


