while True:

    spisok1 = [2, 6, 9, 0, 6, 2, 2, 2, 1]
    spisok2 = []
    spisok4 = []
    spisok3 = set(spisok1)
    kol = 0

    for i in spisok3:
        if (kol := spisok1.count(i)) > 1:
            spisok2.append(kol)
            spisok4.append(i)

    print(f'Дан список {spisok1}')

    if not spisok2:
        print('Все элементы уникальны')
    else:
        for i in range(len(spisok2)):
            print(f'Элемент {spisok4[i]} повторяется {spisok2[i]} раз(а)')

    test = input('\n\nдля завершения нажмите НОЛЬ или ввод для продолжения ')
    if test == '0':
        exit()
