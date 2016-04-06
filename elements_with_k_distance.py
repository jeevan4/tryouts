#FIND DUPLICATE ELEMENTS IN ARRAY WITHIN K DISTANCE FROM EACH OTHER

def find_dup(a,k):
	dic = {}
	eval_list = []
 	for i in a:
		if dic.get(i) != None and dic.get(i) == k:
			print '1st',dic,i
			eval_list.append(True)
		elif dic.get(i) == None:
			print '2nd',i
			dic[i] = 0
		dic = {j:dic[j]+1 for j in dic}
	print eval_list
	if eval_list == []:
		return False
	else:
		return all(eval_list)

a = [1,2,1]
find_dup(a,1)