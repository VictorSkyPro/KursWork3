import json
from pprint import pprint


def main():
    """
    1) Чтение данных из файла операций.
    2) Выборка данных со статусом EXECUTED.
    3) Сортировка по убыванию даты.
    """
    # 1) Чтение данных из файла операций.
    with open('operations.json', mode='r', encoding='utf8') as file:
        data = json.load(file)

    # 2) фильтрация данных. Выбираются только со статусом EXECUTED.
    data = filter(lambda x: x.get('state') == "EXECUTED", data)

    # 3) Сортировка по убыванию даты.
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)


    pprint(list(data))



main()
