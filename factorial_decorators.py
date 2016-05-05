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

def fast_fib(fib):
	cache = {}
	def faster(n):
		if n not in cache:
			print 'inside'
			cache[n] = fib(n)
		return cache[n]
	return faster
			
@fast_fib			
def fib(n):
	if n<=1:
		return n
	else:
		return fib(n-1)+fib(n-2)
