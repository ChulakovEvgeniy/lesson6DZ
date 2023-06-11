# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def input_num(mesage: str) -> int:
    while True:
        num = input(mesage)
        if num.isdigit():
            return int(num)

first_num = input_num('Введите первое число(цифру): ')
size_list = input_num('Введите кол-во элементов: ')
difference = input_num('Введите шаг заполнения: ')

my_list = [first_num]

for elem in range(1, size_list):
    elem = my_list[elem-1] + (size_list-1)*difference
    my_list.append(elem)

print(my_list)