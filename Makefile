# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>

# list all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
.PHONY: list
# required for list
no_targets__:

# install dependencies
setup:
	@pip install -U black flake8 isort
.PHONY: setup

# run isort, black and flake8 for style guide enforcement
isort:
	@isort .
.PHONY: isort

black:
	@black .
.PHONY: black

flake8:
	@flake8
.PHONY: flake8

lint: isort black flake8
.PHONY: lint

# run all even fibonacci sum in src/
run:
	@for even_fib_sum in src/*-*.py; do \
		echo "\n\n⚡️⚡️⚡️ Running $$even_fib_sum ⚡️⚡️⚡️"; \
		python $$even_fib_sum; \
	done;
.PHONY: run

# run the specified even fibonacci sum (e.g.: make src/even_fib_sum_01.py)
%.py: FORCE
	@python $*.py
FORCE:

# clean python object, test and coverage files
clean:
	@find . -type f -name "*.pyc" -delete -print
	@find . -type f -iname '.coverage' -exec rm -rf \{\} + -print
	@find . -type d -iname '.pytest_cache' -exec rm -rf \{\} + -print
	@find . -type d -iname '__pycache__' -exec rm -rf \{\} + -print
	@find . -type d -iname '.benchmarks' -exec rm -rf \{\} + -print
	@find . -type d -iname '*.egg-info' -exec rm -rf \{\} + -print
.PHONY: clean
