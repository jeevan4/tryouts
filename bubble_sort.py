def bubble_sort(a):
	for i in range(len(a)-1):
		for j in range(len(a)-1-i):
			if a[j] > a[j+1]:
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
	return a
a = [10,100,3,5,-1]
b = bubble_sort(a)