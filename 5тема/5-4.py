while True:

    spisok = [2, 6, 9, 2, 1, 459]
    summa = 0

    for i in spisok:
        summa += i

    print(f'дан список {spisok}')
    print(f'Сумма значений списка равна {summa}')
    print(f'Минимальное значение {min(spisok)}')
    print(f'максимальное значение {max(spisok)}')

    test = input('\n\nдля завершения нажмите НОЛЬ или ввод для продолжения ')
    if test == '0':
        exit()
