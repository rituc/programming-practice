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

	def check_palindrome(self):
		slow = self.head
		fast = self.head
		stack = []

		while(fast and fast.next):
			stack.append(slow.data)
			slow = slow.next
			fast = fast.next.next
		if(fast):
			slow = slow.next

		while(slow):
			if slow.data != stack.pop():
				return False
			slow = slow.next
		return True

head = LinkedList

head.push(1)
head.push(2)
head.push(2)
head.push(1)

head.print_list()
print head.check_palindrome()



