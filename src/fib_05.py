#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


def repr():
    return "Iterative 3 by 3, result at the end"


def setup():
    pass


def header():
    return ""


# ---8<---
def even_fib_sum(n):
    a1, a2, a3 = 1, 1, 2
    while a3 < n:
        a1 = a2 + a3
        a2 = a1 + a3
        a3 = a1 + a2
    return (a2 - 1) // 2
