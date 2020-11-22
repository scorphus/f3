#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


try:
    from functools import cache
except ImportError:
    from functools import lru_cache

    cache = lru_cache(maxsize=None)


@cache
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def even_fib_sum(n):
    i = s = 0
    while True:
        f = fib(i)
        if f > n:
            return s
        if f % 2 == 0:
            s += f
        i += 1
