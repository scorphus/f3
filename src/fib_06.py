#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from math import log, sqrt


def setup():
    pass


def header():
    return "from math import log, sqrt\n\n\n"


# ---8<---
def even_fib_sum(n):
    if n < 1:
        return 0
    phi = (1 + sqrt(5)) / 2
    N = (log(n) + log(5) / 2) // log(phi) + 1
    num = (pow(phi, N) - pow(1 - phi, N)) // sqrt(5)
    if num > n:
        N -= 1
    N += 2 - (N % 3)
    return ((pow(phi, N) - pow(1 - phi, N)) // sqrt(5) - 1) / 2
