class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		node = self.head
		while(node):
			print node.data
			node = node.next

	def partition_list(self, x):
		head = self.head
		tail = self.head

		node = self.head

		while(node):
			if node.data < x:
				node.next = head
				head = node
			else:
				tail.next = node
				tail = node
		tail.next = None
		return head

head = LinkedList()
head.push(5)
head.push(6)
head.push(3)
head.push(1)
head.push(2)

print head.print_list()
print "*"*10
print head.partition_list(3)
head.print_list()





