a = [1,4,-3,-4,6,-7,8,-5]
k = 5

sumdic = {}
sumdic[k] = -1
sum1 = 0
for i,elem in enumerate(a):
	sum1 = sum1 + elem
	if sum1 == k and sumdic.get(sum1) != None:
		print a[sumdic[sum1]+1:i+1]
	else:
		sumdic[sum1] = i