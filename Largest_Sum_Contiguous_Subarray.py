def maxSubarraySum(a):
	size = len(a)
	subarr = []
	curmax = 0
	max = 0
	for ind,elem in enumerate(a):
		curmax = curmax + elem
		if curmax >= max:
			max = curmax
			subarr.append(ind)
		elif curmax < 0:
			curmax = 0
			subarr = []		
	print subarr,max
	
maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3])
