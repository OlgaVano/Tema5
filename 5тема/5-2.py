while True:

    n = input('введите целое число - сумма телефона ')
    k = input('введите целое число - ежедневные накопления ')

    if n.isdigit() and k.isdigit():
        n = int(n)
        k = int(k)

        dni = 0
        summa = 0
        while summa < n:
            if (dni + 1) % 7 == 0:
                dni += 1
            summa += k
            dni += 1

        print(dni)
    else:
        print('Попробуйте еще - введите целые числа')

    test = input('\n\nдля завершения нажмите НОЛЬ или ввод для продолжения ')
    if test == '0':
        exit()
