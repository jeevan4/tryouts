class Tree:
	def __init__(self,d):
		self.data = d
		self.left = None
		self.right = None
	
	def setData(self,d):
		self.data = d
	
	def getData(self):
		return self.data

	def setLeft(self,d):
		if self.left == None:
			self.left = Tree(d)
		else:
			current = self.left
			while current.getLeft() != None:
				current = current.getLeft()
			new = Tree(d)
			current.left = new

	def getLeft(self):
		return self.left

	def setRight(self,d):
		if self.right == None:
			self.right = Tree(d)
		else:
			new = Tree(d)
			new.right = self.right
			self.right = new

	def getRight(self):
		return self.right

btree = Tree('a')
btree.setLeft('b')
btree.setRight('c')
btree.getLeft().setRight('d')

print 'root', btree.getData()
print 'leftchild',btree.getLeft().getData()
print 'leftchild right node', btree.getLeft().getRight().getData()
btree.setLeft('x')
print 'leftchild',btree.getLeft().getLeft().getRight()
