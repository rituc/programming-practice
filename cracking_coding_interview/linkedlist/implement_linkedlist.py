class Node:
	def __init__(self, x):
		self.data = x

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, x):
		new_node = Node(x)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		node = self.head
		while(node):
			print node.data
			node = node.next

head = LinkedList()
head.push(1)
head.push(3)
head.push(4)
head.print_list()


