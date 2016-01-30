def quick_sort(a,start,end):
	if start < end:
		pivot = get_pivot(a,start,end)
		quick_sort(a,start,pivot-1)
		quick_sort(a,pivot+1,end)
	return a

def get_pivot(a,start,end):
	pivot = end
	pindex = start
	for i in range(start,end):
		if a[i] < a[pivot]:
			temp = a[i]
			a[i] = a[pindex]
			a[pindex] = temp
			pindex +=1
	temp = a[pivot]
	a[pivot] = a[pindex]
	a[pindex] = temp
	return pindex

a = [1, 6, 5, 7, 8, 9, 2, 0, 4, 3]
print quick_sort(a,0,len(a)-1)