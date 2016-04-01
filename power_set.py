#powerset

a = [1,2,3,4]
p_set = [[]]

for i in a:
	temp = [ j+[i] for j in p_set]
	p_set = p_set+temp
	print p_set