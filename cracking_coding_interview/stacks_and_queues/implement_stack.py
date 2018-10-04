class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, x):
		self.stack.append(x)

	def pop(self):
		if self.is_empty(): return -1
		return self.stack.pop()

	def peek(self):
		if self.is_empty(): return -1
		return self.stack[-1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(5)

print stack.peek()
print stack.pop()
print stack.peek()

