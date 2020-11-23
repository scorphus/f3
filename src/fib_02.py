#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


from itertools import accumulate, cycle, takewhile

try:
    from functools import cache
except ImportError:
    from functools import lru_cache

    cache = lru_cache(maxsize=None)


def repr():
    return "Recursive with iterator tools"


def setup():
    fib.cache_clear()


def header():
    return (
        "from functools import cache\n"
        "from itertools import accumulate, cycle, takewhile\n\n\n"
    )


# ---8<---
@cache
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def even_fib_sum(n):
    return sum(
        takewhile(
            lambda f: f <= n,
            filter(
                lambda f: f % 2 == 0,
                map(fib, accumulate(cycle([1]))),
            ),
        )
    )
