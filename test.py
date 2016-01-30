import sys
#a = [7,1,3,2,9,2,5,4,2,100]
#a = [100, 180, 260, 310, 40, 535, 695]
a = [10,8,7,6]
i = 0

n = len(a)
while i < n-1 :
	while  i < n-1 and a[i] >= a[i+1]:
		i = i+1
	if i == n-1:
		print "No solution"
		sys.exit()
	buy = i
	while i < n-1 and a[i] <= a[i+1]:
		i +=1
	sell = i 
	print buy,sell,a[sell]-a[buy]