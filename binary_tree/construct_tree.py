class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def construct_tree(preorder, inorder):
	if inorder:
		idx = inorder.index(preorder.pop(0))
		root = Node(inorder[idx])
		root.left = construct_tree(preorder, inorder[0:idx])
		root.right = construct_tree(preorder, inorder[idx+1:])
		return root

def main():
	preorder = [3, 9, 20, 15, 7]
	inorder = [9, 3, 15, 20, 7]

	print construct_tree(preorder, inorder)

if __name__ == "__main__":
	main()