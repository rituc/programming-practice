class Node:

	def __init__(self, x):
		self.data = x
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

	def delete_node(self, data):
		node = self.head
		if node.data == data:
			return self.head.next

		while(node.next):
			print "data", node.data
			if node.next.data == data:
				node.next = node.next.next
				return self.head
			node = node.next


		if node.data == data:
			print "data", node.data
			node = None
			return self.head
		return


head = LinkedList()
head.push(1)
head.push(2)
head.push(4)
head.push(3)
head.push()

print "*"*10
head.delete_node(3)
head.print_list()
