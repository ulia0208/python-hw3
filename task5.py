# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

a = int(input('Введите число '))
my_list=[0,1]
my_list2=[0,1]

for i in range(a-1):
    b=my_list[i]+my_list[i+1]
    my_list.append(b)
    c=my_list2[i]-my_list2[i+1]
    my_list2.append(c)

list.reverse(my_list2)
my_list2.remove(0)


my_list3=my_list2+my_list
print(my_list3)