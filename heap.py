a = [3, 8, 6, 20, 7]

def build_heap(a):
	size = len(a)
	print a,size
	parent = (size-2)/2
	for i in range(parent,-1,-1):
		perculatedown(a,i)
	return a
		
def perculatedown(a,i):
	left = (2*i)+1
	right = (2*i)+2
	max = None
	if left <= len(a)-1 or right <= len(a)-1:
		if right > len(a)-1 or a[left] >= a[right]:
			max = left
		else:
			max = right
	if max != None and a[max] > a[i]:
		temp = a[max]
		a[max] = a[i]
		a[i] = temp
		perculatedown(a,max)

a = [3, 8, 6, 20, 7]
b = []
le = len(a)
i = 0	
while i < le:
	a = build_heap(a)
	b.append(a.pop(0))
	print a,b
	i +=1