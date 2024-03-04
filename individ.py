#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def help1():
    """ "
    Функция для вывода списка команд
    """
    print("Список команд:\n")
    print("r1 - Менять слова местами;")
    print("r2 - Найти самые длинные слова из файла;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def error1():
    """ "
    функция для неопознанных команд
    """
    print(f"Неизвестная команда {command}")


def r(filename):
    """ "
    читает файл и передаёт дальше список
    """
    j = []
    with open(filename, "r") as f:
        for line in f:
            j.extend(line.split())

    return j


def r1(filename):
    """ "
    Обращается к функции r() и дальше выводит слова файла меняя их местами
    """
    j = r(filename)

    for i, x in enumerate(j[:-1:2]):
        j[i * 2], j[i * 2 + 1] = j[i * 2 + 1], j[i * 2]

    print(*j)


def r2(filename):
    """ "
    Обращается к функции r() и дальше находит самые длинные слова
    """
    j = r(filename)
    a = max(len(word) for word in j)
    k = [word for word in j if len(word) == a]
    print(k, a)


if __name__ == "__main__":
    help1()

    while True:
        # Запросить команду из терминала.
        command = input(">>> ")
        # Выполнить действие в соответствие с командой.

        match command:
            case "exit":
                break

            case "r1":
                r1("asd.txt")

            case "r2":
                r2("asd.txt")

            case "help":
                help1()

            case _:
                error1()
