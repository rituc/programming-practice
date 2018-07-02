class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def inorder(root):
	if root != None:
		inorder(root.left)
		print root.val,
		inorder(root.right)


def preorder(root):
	if root != None:
		print root.val,
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root != None:
		postorder(root.left)
		postorder(root.right)
		print root.val,

def level_order(root):
	if root is None:
		return
	queue = []
	queue.append(root)
	while(len(queue)>0):
		print queue[0].val,
		node = queue.pop(0)

		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(root.right)

def vertical_order_util(root, hash_map, hori_dist):
	if root is None:
		return

	try:
		hash_map[hori_dist].append(root.val)
	except:
		hash_map[hori_dist] = [root.val]

	vertical_order_util(root.left, hash_map, hori_dist-1)
	vertical_order_util(root.right, hash_map, hori_dist + 1)

# 43 460 3871 4698 8399 504 4421 7515 -1 4167 5727 -1 -1 3096 434 7389 2667 5661 1969 7815 4292 3006 9750 6693 -1 6906 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1


def vertical_order(root):
	hash_map = dict()
	hori_dist = 0
	vertical_order_util(root, hash_map, hori_dist)

	print hash_map.values()

	for indx, value in enumerate(sorted(hash_map)):
		for i in hash_map[value]:
			print i,
		print



def height(root):
	h = 0
	if root!=None:
		h = max(height(root.left), height(root.right)) + 1
	return h

def main():
	# root = Node(1)
	# root.left = Node(2)
	# root.right = Node(3)
	# root.left.left = Node(4)
	# root.left.right = Node(5)

	# print "Inorder"
	# inorder(root)
	# print "\nPre-Order:"
	# preorder(root)
	# print "\nPost-Order:"
	# postorder(root)
	# print "\n Level Order:"
	# level_order(root)

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.right.left.right = Node(8)
	root.right.right.right = Node(9)

	print "\n Vertical Order:"
	vertical_order(root)

	print "\nHeight of tree: ",  height(root)

if __name__ == "__main__":
	main()


