#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

import logging
import os
from importlib import import_module
from timeit import timeit

log_level = getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper())
logging.basicConfig(level=log_level)

MODULES = ["fib_01", "fib_02"]
N = int(1e300)
TIMEIT_NUMBER = int(1e4)


def load_modules():
    for module in MODULES:
        yield module, import_module(module)


def read_source_code(file_path):
    with open(file_path) as fd:
        return fd.read().split("# ---8<---", 1)[1].strip()


def gen_code_block(module, time_spent):
    file_base_name = os.path.basename(module.__file__)
    source_code = read_source_code(module.__file__)
    return f"""\n
{{{{<highlight python>}}}}
# {file_base_name}
{module.header()}{source_code}


# Time spent: {time_spent:0.6f}ms
{{{{</highlight>}}}}
"""


if __name__ == "__main__":
    code_blocks = ""
    for module_name, module in load_modules():
        time_spent = timeit(
            stmt=f"module.even_fib_sum({N})",
            setup="module.setup()",
            globals={"module": module},
            number=TIMEIT_NUMBER,
        )
        time_spent = time_spent * 1e3 / TIMEIT_NUMBER
        code_blocks += gen_code_block(module, time_spent)
        logging.info(
            "%s: %0.6f (%d)",
            module_name,
            time_spent,
            module.even_fib_sum(N),
        )
    with open("code_blocks.md", "w") as fd:
        fd.write(code_blocks.lstrip())
