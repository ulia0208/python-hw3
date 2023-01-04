# # Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения

# a=int(input('Введите число A '))
# b=int(input('Введите число B '))
# c=int(input('Введите число C '))

# print(f"{a}x²+{b}x+{c}")

# d=b**2-(4*a*c)

# print(d)

# if d<0:
#     print('Корней нет')

# else:
#     x1=((-1*b)+(d**(1/2)))/(2*a)
#     x2=((-1*b)-(d**(1/2)))/(2*a)

`# print(f"x1={x1}")`
# print(f"x2={x2}")





# import math
# equation = '3 *x**2 +  5*x - 6 = 0'

# def ceate_koef(equation: str):
#     new_equation = equation.replace(' ', '').replace('=0', '')\
#         .replace('+', ' ').replace('-', ' -')

#     new_equation = new_equation.split()
#     new_list = []
#     for item in new_equation:
#         if item.startswith('x'):
#             new_list.append(1)
#         elif item.startswith(' -x'):
#             new_list.append(-1)
#         else:
#             new_list.append(item.split('*x')[0])
#     return new_list
# def solve_equation()



a=str(input('Введите число '))
print(a.split('.'))