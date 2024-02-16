#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    elements = list(map(int, input('Введите ряд из чисел, через пробел: ').split()))
    indexer = int(input('Введите число, ищющее индексы элементы списка: '))

    if indexer in elements:
        index = elements.index(indexer)+1
        print('Индекс заданного элемента:', index)
    else:
        print('Заданного элемента нет в списке')
