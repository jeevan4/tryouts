def fib(a):
	if a <= 1:
		return a
	else:
		return fib(a-1)+fib(a-2) + 1

print fib(9)
'''sum = 0		
for i in range(12):
	print fib(i)
	sum = sum +fib(i)
print 'sum',sum
'''