#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
from math import sin

EPS = 10**-7
PI = 3.14


def check_result(x):
    y = x / 2
    print(f"Контрольное значение функции: {y}")


def sum_inf(x):
    n = 1
    epsilon = 1e-7
    s = (-1) ** (n + 1) * sin(n * x) / n
    summ = s

    while abs(s) > epsilon:
        n += 1
        s = (-1) ** (n + 1) * sin(n * x) / n
        summ += s

    print(f"Значение суммы ряда: {summ}")


def main():
    x = PI / 2
    th1 = Thread(target=sum_inf(x))
    th2 = Thread(target=check_result(x))
    th1.start()
    th2.start()


if __name__ == "__main__":
    main()
