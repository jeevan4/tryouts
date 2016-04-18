a = [1,4,-3,-4,6,-7,8,-5]
k = 5

def seqsum(a,k):
	dic = {}
	cumsum = 0
	dic[cumsum] = -1
	for ind,elem in enumerate(a):
		cumsum = cumsum+elem
		if cumsum - k in dic:
			print a[dic[cumsum-k]+1:ind+1]
		else:
			dic[cumsum] = ind
