class Node:

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def is_identical(root_a, root_b):
	if root_a is None and root_b is None: return True
	if root_a is not None or root_b is not None: return root_a.val == root_b.val and is_identical(root_a.left, root_b.left) and is_identical(root_a.right, root_b.right)
	return False

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)


root3 = Node(1)
root3.left = Node(5)
root3.right = Node(7)

print  is_identical(root1, root2)
print  is_identical(root1, root3)
