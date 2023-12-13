#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outer_function():
    def inner_function(x):
        return x + 3
    return inner_function


if __name__ == "__main__":
    cnt = outer_function()

    k = float(input("Введите значение k: "))

    result = cnt(k)

    print(f"Результат: {result}")
