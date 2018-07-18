class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def is_mirror(p, q):
	if p is None and q is None: return True
	if p is not None and q is not None: return p.val == q.val and is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
	return False


def is_symmetric(root):
	if root:
		return is_mirror(root.left, root.right)
	return True



root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print is_symmetric(root1)
print is_symmetric(root2)