class Node:

	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

def create_tree(a, start, end):
	if(end<start):
		return
	mid = (start + end)/2
	node = Node(a[mid])
	node.left = create_tree(node.left, start, mid-1)
	node.right = create_tree(node.right, mid+1, end)
	return node

