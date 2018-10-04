class Stack:
	def __init__(self):
		self.stack = []
	def is_empty(self):
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		if self.is_empty():
			return "Empty"
		self.stack.pop()

	def peek(self):
		if self.is_empty():
			return "Empty"
		return self.stack[-1]

	def size(self):
		return len(self.stack)
