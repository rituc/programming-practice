class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	#insert node in the beginning of list
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head;
		self.head = new_node

	def delete_node(self, node):
		curr = self.head
		while(curr!=node):
			curr = curr.next

		curr.next = curr.next.next





