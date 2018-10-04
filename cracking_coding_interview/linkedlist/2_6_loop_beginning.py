class Node:
	def __init__(self, data):
		self.x = data
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

	def find_loop(self):
		slow = self.head
		fast = self.head

		while(fast and fast.next):
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				break

		if not fast and not fast.next: return None
		slow = self.head
		while slow != fast:
			slow = slow.next
			fast = fast.next
		return fast



head = LinkedList()
head.push(5)
head.push(6)
head.push(3)
head.push(1)
head.push(2)

print head.print_list()
print "*"*10
print head.find_loop(3)
head.print_list()