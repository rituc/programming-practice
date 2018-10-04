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

	def kth_last(self, k):

		if k<=0 : return None
		curr = self.head
		runner = self.head

		for i in range(k):
			if runner == None: return None
			runner = runner.next

		if runner == None: return None

		while(runner):
			runner = runner.next
			curr = curr.next

		return curr.data

head = LinkedList()
head.push(1)
head.push(2)
head.push(3)
head.push(4)
head.push(5)

print head.print_list()
print "*"*10
print head.kth_last(3)
# head.print_list()




