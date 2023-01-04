# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

a = int(input('Введите число '))
my_list=[]

for i in range(a):
    while a>1:  
        b=a%2
        a=int(a/2)
          
        # print(f"{i}-b{b}") 
        my_list.append(b)

my_list.append(a)
list.reverse(my_list)
# print(my_list)  


print(" ".join(map(str, my_list)))  

