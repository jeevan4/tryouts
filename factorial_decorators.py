def fast_fact(fact):
	cache = {}
	def fast(n):
		print cache
		if n not in cache:
			cache[n] = fact(n)
		return cache[n]
	return fast

@fast_fact
def fact(n):
	if n <= 1:
		return 1
	else:
		return n*fact(n-1)