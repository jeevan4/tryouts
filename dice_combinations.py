def PrintDiceCombinations(num_dice):
	pools = [(1,2,3,4,5,6)] * num_dice
	result = [[]]
	for pool in pools:
		result = [x+[y] for x in result for y in pool]
	for res in result:
		yield tuple(res)