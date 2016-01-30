import sys
def draw_tree(h):
	for i in range(h):
		print ' '*(h-i),'*'*((2*i)+1)

draw_tree(int(sys.argv[1]))	