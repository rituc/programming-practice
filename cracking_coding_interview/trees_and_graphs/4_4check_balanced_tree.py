class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def tree_height(node):
	if node:
		return max(tree_height(node.left), tree_height(node.right)) + 1
	return 0

def check_balanced_tree(node):
	if node:
		lh = tree_height(node.left)
		rh = tree_height(node.right)
		return abs(lh-rh) <= 1
	return True

root = Node(2)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print check_balanced_tree(root)