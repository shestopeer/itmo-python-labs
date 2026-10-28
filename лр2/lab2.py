from csv import reader
from random import sample
from xml.dom import minidom
import os

with open('books.csv') as f:
    table = list(reader(f, delimiter=';'))[1:]
    table_limited = [row for row in table if int(row[6][6:10]) in [2014, 2016, 2017]]

def find_string(searchline, string):
    return string.lower().find(searchline.lower())

def task_1():
    os.system('cls')
    print('Длиннее 30:', sum(len(row[1]) > 30 for row in table))
    input('Нажмите Enter для продолжения...')

def task_2(table_limited):
    os.system('cls')
    searchline = input('Автор: ')
    if searchline in ['0', '']:
        return 0
    flag = 0
    for row in table_limited:
        if find_string(searchline, row[3]) != -1:
            print(row[1], '|', row[3])
            flag += 1
    if flag == 0:
        print('Ничего не найдено!')
    input('Нажмите Enter для продолжения...')

def task_3():
    os.system('cls')
    with open('bibliography.txt', 'w', encoding='utf-8') as output:
        for i, row in enumerate(sample([r for r in table if r[3]], 20), 1):
            output.write(f'{i}. {row[3]}. {row[1]} - {row[6][6:10]}\n')
    input('Файл bibliography.txt успешно создан! Нажмите Enter для продолжения...')

def task_4():
    os.system('cls')
    with open('currency.xml', 'r', encoding='windows-1251') as xml_file:
        dom = minidom.parseString(xml_file.read())
    nodes = dom.getElementsByTagName('Valute')
    names = []
    for node in nodes:
        nominal = int(node.getElementsByTagName('Nominal')[0].firstChild.data)
        if nominal == 1:
            name = node.getElementsByTagName('Name')[0].firstChild.data
            names.append(name)
    with open('currency_names.txt', 'w', encoding='utf-8') as file:
        for i, name in enumerate(names, 1):
            file.write(f'{i}. {name}\n')
    input('Файл currency_names.txt успешно создан! Нажмите Enter для продолжения...')


def task_5():
    os.system('cls')
    tags = set()
    for row in table:
        for tag in row[12].split('#'):
            tag = tag.strip()

            if tag != '':
                tags.add(tag)
    print(len(tags), 'тегов')
    top = {}
    for row in table:
        name = row[1]
        count = int(row[8])
        if name not in top:
            top[name] = 0
        top[name] += count
    popular = sorted(top, key=top.get, reverse=True)
    with open('popular_books.txt', 'w', encoding='utf-8') as file:
        for i, name in enumerate(popular[:20], 1):
            file.write(f'{i}. {name}\n')
    input('Файл popular_books.txt успешно создан! Нажмите Enter для продолжения...')

while True:
    os.system('cls')
    print('1. Задание 1')
    print('2. Задание 2')
    print('3. Задание 3')
    print('4. Задание 4')
    print('5. Дополнительное задание')
    print('0. Выход')
    choice = input('Выберите задание: ')
    match choice:
        case '1':
            task_1()
        case '2':
            task_2(table_limited)
        case '3':
            task_3()
        case '4':
            task_4()
        case '5':
            task_5()
        case '0':
            break
        case _:
            print('Неверный выбор')