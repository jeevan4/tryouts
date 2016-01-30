def bubble_sort(a):
	for i in range(len(a)-1):
		for j in range(len(a)-1-i):
			if a[j] > a[j+1]:
				temp = a[j+1]
				a[j+1] = a [j]
				a[j] = temp
	return a
	

a = bubble_sort([1, 6, 5, 7, 8, 9, 2, 0, 4, 3])
print a
start = 0
end = len(a)-1
sum_num = False
while start != end and sum_num == False:
	if a[start] + a[end] == 2:
		sum_num = True
	elif a[start] + a[end] < 2:
		start += 1
	elif a[start] + a[end] > 2:
		end = end - 1
print sum_num