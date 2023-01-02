# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import randint
from random import uniform

a = int(input('Введите число '))



my_list = [round(uniform(0,10),2) for i in range (a)]

my_list2=[]

for i in range(a):
    if my_list[i]%1>0:
        my_list2.append(round(my_list[i]%1,2))



print(f"Список чисел - {my_list}")
# print(my_list2)


min=my_list2[0]
for i in range(len(my_list2)):
    
    if (my_list2[i]*100)%10 != 0:

        if my_list2[i]< min:
            min=my_list2[i]
# print(min)

max=my_list2[0]
for i in range(len(my_list2)):
    
    if (my_list2[i]*100)%10 != 0:

        if my_list2[i] > max:
            max=my_list2[i]


# print(max)

print(f"Разница между максимальным и минимальным - {max-min}")
