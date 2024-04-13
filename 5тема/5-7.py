while True:
    spisok = [5, 6, 7, 1, 2, 3, 4]
    poisk_i = input(f'Дан спикок {spisok}\n укажите одно из значений для поиска ')

    if poisk_i.isdigit() and int(poisk_i) in spisok:
        poisk_i = int(poisk_i)
        x = 0
        nachalo = 0
        konec = len(spisok) - 1
        index_cent = 0
        while poisk_i not in [x, spisok[nachalo], spisok[konec]]:
            index_cent = (konec - nachalo) // 2 + nachalo
            x = spisok[index_cent]
            if (spisok[index_cent] - spisok[nachalo] > 0 and poisk_i < spisok[index_cent]):
                konec = index_cent
            elif (spisok[konec] - spisok[index_cent] > 0 and poisk_i < spisok[konec]):
                nachalo = index_cent
            elif (spisok[index_cent] - spisok[nachalo] > 0 and poisk_i > spisok[index_cent]):
                nachalo = index_cent
            else:
                konec = index_cent
        else:
            if poisk_i == x:
                print(f'Число {poisk_i} находиться на {index_cent + 1} месте в списке')
            elif poisk_i == spisok[nachalo]:
                print(f'Число {poisk_i} находиться на {nachalo + 1} месте в списке')
            elif poisk_i == spisok[konec]:
                print(f'Число {poisk_i} находиться на {konec + 1} месте в списке')
    else:
        print('Попробуйте еще - введите целые числа из заданного списка')
    test = input('\n\nдля завершения нажмите НОЛЬ или ввод для продолжения ')
    if test == '0':
        exit()
