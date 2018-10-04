class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

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

	def delete_middle_node(self, node):
		if node is None and node.next is None: return False
		node.data = node.next.data
		node.next = node.next.next
		return True

head = LinkedList()
head.push(1)
head.push(2)
head.push(3)
head.push(4)
head.push(5)

print head.print_list()
print "*"*10
print head.delete_middle_node()
head.print_list()
