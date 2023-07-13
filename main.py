import json
from pprint import pprint


def main():

    with open('operations.json', mode='r', encoding='utf8') as file:
        data = json.load(file)


    pprint(data)



main()
