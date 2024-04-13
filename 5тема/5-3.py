while True:

    n = input('введите количество чисел ')

    if n.isdigit():
        n = int(n)

        i = 2
        a = 1
        b = 1
        print(a, b, end=" ")
        while i <= n:
            a, b = b, a + b
            print(b, end=" ")
            i += 1

    else:
        print('Попробуйте еще - введите целые числа')

    test = input('\n\nдля завершения нажмите НОЛЬ или ввод для продолжения ')
    if test == '0':
        exit()
