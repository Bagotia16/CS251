class Node(object):
	"""
	Node contains two objects - a left and a right child, both may be a Node or both None,
	latter representing a leaf
	"""
	def __init__(self, left=None, right=None):
		super(Node, self).__init__()
		self.left = left
		self.right = right

	def __str__(self):
		"""
		Default inorder print
		"""
		if self.left is None and self.right is None:
			return "(   )"
		else:
			return "( " + str(self.left) + " " + str(self.right) + " )"

	def __eq__(self, other):
		if self.left is None and self.right is None:
			return other.left is None and other.right is None
		elif other.left is None and other.right is None:
			return False
		else:
			return self.left == other.left and self.right == other.right


def mirrorTree(node):
	"""
	Returns the mirror image of the tree rooted at node
	"""

	c=Node(node.left,node.right)
	if c.left is None and c.right is None:
		return c 

	temp=c.left
	c.left=c.right
	c.right=temp

	c.right=mirrorTree(c.right)
	c.left=mirrorTree(c.left)

	return c
	pass


def allTrees(n):
	"""
	Returns a list of all unique trees with n internal nodes
	"""
	l=[]
	if n==0:
		
		l.append(Node(None,None))
		return l

	for k in range(n):
		l+=[Node(x,y) for x in allTrees(k) for y in allTrees(n-1-k)]

	return l

	pass


def allSymTrees(n):
	"""
	Returns a list of all unique symmetrical trees with n internal nodes
	"""
	l=[]
	if n==0:
		
		l.append(Node(None,None))
		return l

	elif n%2==0:
		return []

	else:
		l+=[Node(x,mirrorTree(x)) for x in allTrees((n-1)//2) if x not in allSymTrees((n-1)//2)]

		l+=[Node(x,x) for x in allSymTrees((n-1)//2)]

	return l

	pass


if __name__ == '__main__':
	for x in allSymTrees(int(input())):
		print(x)
	node = Node(Node(Node(), Node()), Node())
	print(node)