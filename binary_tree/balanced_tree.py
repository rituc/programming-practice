class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def height(root):
	if root:
		return max(height(root.left), height(root.right)) + 1
	return 0

def is_balanced(root):
	if root:
		lh = height(root.left)
		rh = height(root.right)
		return abs(lh - rh) <= 1
	return True

def dfs_height(root):
	if root:
		left_height = dfs_height(root.left)
		if left_height == -1: return -1
		right_height = dfs_height(root.right)
		if right_height == -1: return -1
		if abs(left_height - right_height) > 1: return -1
		return max(left_height, right_height) + 1
	return 0

def is_balanced1(root):
	return dfs_height(root) != 1



root = Node(2)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(3)

root1.left.left.left = Node(4)
root1.left.left.right = Node(4)

root2 = None

# root3 = Node(1)
# root3.left = Node(2)
# root3.right = Node(2)
# root3.left.left = Node(3)
# root3.left.right = Node(3)


# [1,2,2,3,None,None,3,4,None,None,4]

print is_balanced1(root)
print is_balanced1(root1)
print is_balanced1(root2)