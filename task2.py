
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint
a=int(input('Введите число '))

my_list=[randint(-10,10) for i in range(a)]
print(my_list)

my_list2=[]
print(a)
for i in range(int(a/2)+1):
    my_list2.append(my_list[i] * my_list[a-i-1])

print(my_list2)
