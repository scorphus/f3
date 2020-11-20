from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
	return n if n < 4 else fib(n - 2) + fib(n - 1)


def even_fib_sum(n):
	i = s = 0
	while True:
		f = fib(i)
		if f > n:
			return s
		if f % 2 == 0:
			s += f
		i += 1


if __name__ == "__main__":
    from timeit import timeit
    print(even_fib_sum(1e300))
    t_number = int(1e4)
    t_spent = timeit("even_fib_sum(1e300)", globals=globals(), number=t_number)
    t_spent = t_spent * 1e3 / t_number
    print(f"Time spent: {t_spent:.6f}ms")
    with open("time_spent.txt", "w") as fd:
        fd.write(f"# Time spent: {t_spent*1e3:.6f}ms")
