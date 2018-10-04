"""Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo­rithm to create a binary search tree with minimal height."""

class Node:

	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None

def create_bst(a):
	if not a: return None
	mid = len(a)/2
	root = Node(a[mid])
	root.left = create_bst(a[:mid])
	root.right = create_bst(a[mid+1:])
	return


