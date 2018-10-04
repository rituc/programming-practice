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

	def delete_duplicate(self):
		curr = self.head
		while(curr):
			runner = curr
			while(runner.next):
				if runner.next.data == curr.data:
					runner.next = runner.next.next
				else:
					runner = runner.next
			curr = curr.next


	def delete_dups_using_hash(self):
		track = []
		node = self.head
		while(node.next):
			if node.next.data in track:
				node.next =node.next.next
			else:
				track.append(node.next.data)
				node = node.next

	def remove_dups(self):
		hash_count = dict()
		prev = self.head
		while (prev.next):
			curr = prev.next
			if curr.data in hash_count:
				prev.next = curr.next
			else:
				hash_count[curr.data] = 1
				prev = prev.next
		return self.head

head = LinkedList()
head.push(1)
head.push(1)
head.push(2)
head.push(2)
head.push(3)
head.push(3)
head.push(3)

print head.print_list()
head.remove_dups()
print "="*10
print head.print_list()


