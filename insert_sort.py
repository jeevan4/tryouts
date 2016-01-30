def insertion_sort(a):
	for i in range(len(a)):
		ind = i
		while ind > 0 and a[ind] < a[ind-1]:
			temp = a[ind]
			a[ind] = a[ind-1]
			a[ind-1] = temp
			ind = ind -1
	return a

a = [5,4,1,3]
print insertion_sort(a)