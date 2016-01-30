
a = [6,3,2,1]
n = len(a)

i = 0 

while i < n-1:
	while i < n-1 and a[i] >= a[i+1]:
		i +=1
	if i == n-1:
		print "no solution"
		break
	buy = i
	while i < n-1 and a[i] <= a[i+1]:
		i +=1
	sell = i
	print buy,sell,a[sell]-a[buy]
