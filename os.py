#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def file_info(directory, filename):
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        print(f"Файл '{filename}' существует.")
        print(f"Размер файла: {file_size} байт")
    else:
        print(f"Файл '{filename}' не существует в указанной директории.")


if __name__ == "__main__":
    directory_path = input("Введите путь к файлу:")
    file_name = input("Введите название файла:")

    if os.path.isdir(directory_path):
        file_info(directory_path, file_name)
    else:
        print("Указанная директория не существует.")
