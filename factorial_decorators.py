'''
One call to factorial results in the cache building up for all numbers < n. 
Next time you invoke factorial for a number < n, the result is not computed but fetched from the cache. 
This makes it easy to separate out the cache maintaining logic from the function being decorated.
'''
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
