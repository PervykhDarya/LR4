#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import sys



def get_product():
    """
    Запросить данные о товаре
    """
    name = input("Название товара? ")
    shop = input("Название магазина? ")
    coast = int(input("Введите его цену "))
    return {
        'name': name,
        'shop': shop,
        'coast': coast,
    }


def display_products(products):
    """
     Отобразить список продуктов
    """
    if products:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Наименование товара",
                "Название магазина",
                "Стоимость"
            )
        )
        print(line)

        for idx, product in enumerate(products, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    product.get('name', ''),
                    product.get('shop', ''),
                    product.get('coast', 0)
                )
            )
        print(line)

    else:
        print("Список продуктов пуст")


def save_products(file_name, products):
    """
    Сохранить всех работников в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(products, fout, ensure_ascii=False, indent=4)


def load_products(file_name):
    """
    Загрузить все продукты из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    """
    Главная функция программы
    """
    products = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            product = get_product()
            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('name', ''))
        elif command == "list":
            display_products(products)
        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            save_products(file_name, products)
        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            products = load_products(file_name)
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()