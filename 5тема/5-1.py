import math as m

n = input('введите целое число итераций (10 - хорошо)')
x = input('введите угол для расчета его синуса - целым числом ')

rez = 0
if x.isdigit() and n.isdigit():
    x = int(x)
    n = int(n)

    for i in range(n + 1):
        z = (2 * i + 1)
        rez += (-1) ** i * (x ** z) / (m.factorial(z))

    print(rez)
else:
    print('Попробуйте еще - введите целые числа')
