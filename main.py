import json
from pprint import pprint

def display_info(operation):
    """Формирует вывод данных в удобном пользователю формате"""

    out = f"{date_dd_mm_eeee(operation['date'])} {operation['description']} \n" \
          f" {operation['from']} -> {operation['to']} \n " \
          f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']} \n"

    print(out)

def date_dd_mm_eeee(date):
    """Формирует удобный формат даты.
    Пример: 2019-12-07 -> 07.12.2019.
    1) выбирает первые 10 символов даты.
    2) разделяет дату по символу '-'.
    3) переворачивает элементы списка.
    4) объединяет элементы через символ '.'
     """
    return '.'.join(date[:10].split('-')[::-1])


def main():
    """
    1) Чтение данных из файла операций.
    2) Выборка данных со статусом EXECUTED.
    3) Сортировка списка по убыванию даты.
    4) Выводим список из последних пяти элементов.
    """
    # 1) Чтение данных из файла операций.
    with open('operations.json', mode='r', encoding='utf8') as file:
        data = json.load(file)

    # 2) фильтрация данных. Выбираются только со статусом EXECUTED.
    data = filter(lambda x: (x.get('state') == "EXECUTED" and x.get('from')), data)

    # 3) Сортировка по убыванию даты.
    data = sorted(data, key=lambda x: x.get('date'), reverse=True)

    # 4) Выводим список из последних пяти элементов.
    for operation in data[:5]:
        display_info(operation)


main()
