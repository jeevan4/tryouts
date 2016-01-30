a = [7,1,3,2,9,2,5,4,2,100]
 
max = a[len(a)-1]
diff = 0 
for i in range(len(a)-2,-1,-1):
	if a[i] > max:
		max = a[i]
	else:
		if max - a[i] > diff:
			diff = max-a[i]
			pair = (a[i],max)

print diff,pair