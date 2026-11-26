from itertools import combinations


class Item:
    def __init__(self, symbol, weight, value):
        self.symbol = symbol
        self.weight = weight
        self.value = value


ROWS, COLS = 2, 4
START_POINTS = 10

ANTIDOT = Item('d', 1, 10)  # антидот

ITEMS = [
    Item('r', 3, 25),   # винтовка
    Item('p', 2, 15),   # пистолет
    Item('a', 2, 15),   # боекомплект
    Item('m', 2, 20),   # аптечка
    Item('i', 1, 5),    # ингалятор
    Item('k', 1, 15),   # нож
    Item('x', 3, 20),   # топор
    Item('t', 1, 25),   # оберег
    Item('f', 1, 15),   # фляжка
    Item('s', 2, 20),   # еда
    Item('c', 2, 20),   # арбалет
]

TOTAL = sum(item.value for item in ITEMS) + ANTIDOT.value


def knapsack(items, capacity):
    def node_count(i, weight, value):
        j = i
        while j < len(items) and weight + items[j].weight <= capacity:
            value += items[j].value
            weight += items[j].weight
            j += 1
        if j < len(items):
            value += (capacity - weight) * (items[j].value / items[j].weight)
        return value

    def branch_bound(i, weight, value, taken):
        nonlocal max_value, best
        if value > max_value:
            max_value = value
            best = taken
        if i == len(items) or node_count(i, weight, value) <= max_value:
            return
        if weight + items[i].weight <= capacity:
            branch_bound(i + 1, weight + items[i].weight,
                         value + items[i].value, taken + [items[i]])
        branch_bound(i + 1, weight, value, taken)

    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    best = []
    branch_bound(0, 0, 0, [])
    return best


def score(taken):
    value = sum(item.value for item in taken)
    return START_POINTS + value - (TOTAL - value)


def symbols(taken):
    result = []
    for item in taken:
        result.append(item.symbol)
    return result


def print_inventory(taken):
    cells = []
    for item in sorted(taken, key=lambda x: x.weight, reverse=True):
        cells += [item.symbol] * item.weight
    for r in range(ROWS):
        line = ''
        for c in cells[r * COLS:(r + 1) * COLS]:
            line += '[' + c + '] '
        print(line)


def all_combinations(items, capacity):
    result = []
    for n in range(len(items) + 1):
        for combo in combinations(items, n):
            if sum(item.weight for item in combo) <= capacity:
                taken = [ANTIDOT] + list(combo)
                if score(taken) > 0:
                    result.append(taken)
    return result


if __name__ == '__main__':
    capacity = ROWS * COLS - ANTIDOT.weight

    taken = [ANTIDOT] + knapsack(ITEMS, capacity)
    print_inventory(taken)
    print('Итоговые очки выживания:', score(taken))

    print()
    print('Допзадание 1: инвентарь на 7 ячеек')
    taken7 = [ANTIDOT] + knapsack(ITEMS, 7 - ANTIDOT.weight)
    print('Лучший набор:', symbols(taken7))
    print('Очки:', score(taken7))
    if score(taken7) <= 0:
        print('Решения с положительным счётом нет')

    print()
    print('Допзадание 2: все комбинации с положительным счётом')
    combos = all_combinations(ITEMS, capacity)
    for taken in combos:
        print(score(taken), symbols(taken))
    print('Всего комбинаций:', len(combos))
