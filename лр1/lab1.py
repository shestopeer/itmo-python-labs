import time
import os

BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
BLACK = '\u001b[40m'
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
GREY = '\u001b[100m'


def flag():
    pixel = '    '
    length = 10
    height = 9

    for i in range(height):
        if i < height // 3:
            print(f"{RED}{pixel * length}{RESET}")
        elif i < 2 * height // 3:
            print(f"{WHITE}{pixel * length}{RESET}")
        else:
            print(f"{BLUE}{pixel * length}{RESET}")


def pattern():
    pixel = '  '
    length = 3
    motif = [
        '+---+---+',
        '-+-+-+-+-',
        '--+---+--',
        '-+-+-+-+-',
        '+---+---+'
    ]
    for row in motif:
        for char in row[:-1] * length:
            if char == '+':
                print(f"{BLACK}{pixel}{RESET}", end='')
            elif char == '-':
                print(f"{WHITE}{pixel}{RESET}", end='')
        if row[-1] == '+':
            print(f"{BLACK}{pixel}{RESET}", end='')
        elif row[-1] == '-':
            print(f"{WHITE}{pixel}{RESET}", end='')
        print()


def frame(n):
    pixel = '  '
    start_row = 3
    start_col = 30
    motif = [
        '-----',
        '-111-',
        '-111-',
        '-111-',
        '-----',
        '-222-',
        '-222-',
        '-222-',
        '-----',
        '-333-',
        '-333-',
        '-333-',
        '-----',
    ]

    red = GREY
    yellow = GREY
    green = GREY
    if n == 1:
        red = RED
    elif n == 2:
        red = RED
        yellow = YELLOW
    else:
        green = GREEN

    for row_number, row in enumerate(motif):
        print(f'\u001b[{start_row + row_number};{start_col}H', end='')
        for char in row:
            if char == '-':
                print(f'{BLACK}{pixel}{RESET}', end='')
            elif char == '1':
                print(f'{red}{pixel}{RESET}', end='')
            elif char == '2':
                print(f'{yellow}{pixel}{RESET}', end='')
            else:
                print(f'{green}{pixel}{RESET}', end='')
        print()


def animation():
    for cycle in range(3):
        for frames in range(1, 4):
            os.system('cls')
            frame(frames)
            time.sleep(1.5)
    print()


def diagram():
    with open('sequence.txt') as file:
        data = []
        for line in file:
            data.append(float(line))
    even = []
    odd = []
    for num, value in enumerate(data):
        if (num + 1) % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    sum_even = 0
    sum_odd = 0
    for i in even:
        sum_even += abs(i)
    for i in odd:
        sum_odd += abs(i)
    percent_even = sum_even / (sum_even + sum_odd) * 100
    percent_odd = 100 - percent_even
    pixel = ' '
    length_even = round(percent_even)
    length_odd = 100 - length_even
    print(f'Нечётные: {RED}{pixel * length_odd}{RESET} {percent_odd:.2f}%')
    print(f'Чётные:   {BLUE}{pixel * length_even}{RESET} {percent_even:.2f}%')


def graph():
    os.system('cls')
    start_row = 2
    start_col = 10
    length_axis = 10
    for row in range(start_row, start_row + length_axis):
        print(f'\u001b[{row};{start_col}H{WHITE} {RESET}', end='')

    for col in range(start_col, start_col + length_axis * 2):
        print(f'\u001b[{start_row + length_axis};{col}H{WHITE} {RESET}', end='')

    for y in range(1, length_axis + 1):
        x = y / 2
        row = start_row + length_axis - y
        col = start_col + int(2 * x)
        print(f'\u001b[{row};{col}H{BLUE} {RESET}', end='')

    for y in range(1, length_axis + 1):
        row = start_row + length_axis - y
        print(f'\u001b[{row};{start_col - 3}H{y}', end='')
        
    for y in range(1, length_axis * 2):
        x = y / 2
        col = start_col + int(2 * x)
        if y % 2 == 0:
            print(f'\u001b[{start_row + length_axis + 1};{col}H{int(x)}', end='')

    print(f'\u001b[{start_row + length_axis + 1};{start_col - 2}H0', end='')
    print(f'\u001b[{start_row - 1};{start_col}Hy', end='')
    print(f'\u001b[{start_row + length_axis};{start_col + length_axis * 2 + 1}Hx', end='')
    print(f'\u001b[{start_row - 1};{start_col + 8}Hy = 2x', end='')
    print(f'\u001b[{start_row + length_axis + 3};1H')


flag()
print()
pattern()
input('Нажмите Enter для продолжения...')
animation()
diagram()
input('Нажмите Enter для продолжения...')
graph()
