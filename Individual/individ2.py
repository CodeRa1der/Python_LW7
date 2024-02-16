#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    list = list(map(int, input('Введите целые элементы через пробел: ').split()))
    even = []
    odd = []
    count = 0
    sum = 0
    min = 0
    minnum = 0

    for i in range(len(list)):
        k = list[i]
        # Запись четных и нечетных элементов
        if (list.index(k) + 1) % 2 == 0:
            even.append(list[i])
        else:
            odd.append(list[i])
        # Задача №1
        if list.index(k) == 0:
            min = abs(list[i])
            minnum = list[i]
        if abs(list[i]) < min:
            min = abs(list[i])
            minnum = list[i]
        # Задача №2
        if list[i] == 0:
            count += 1
        if count != 0:
            sum += list[i]

    print('')
    print('Минимальный по модулю элемент списка:', minnum)
    if sum != 0:
        print('Сумма элементов после первого нуля:', sum)
    else:
        print('В списке нет элементов, равных нулю')
    print('Реорганизованный список:')
    print(even + odd)
