from sys import maxsize

# def create_stack():
# 	stack = []
# 	return stack
#
# def is_empty(stack):
# 	return len(stack) == 0
#
# def push(stack, item):
# 	stack.append(item)
#
# def pop(stack):
# 	if(is_empty(stack)):
# 		return str(-maxsize+1)
# 	return stack.pop()
#
# stack = create_stack()
# push(stack, 10)
# push(stack, 20)
#
# print pop(stack)

class Stack:

	def __init__(self):
		self.stack = []

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if (self.is_empty()):
			return str(-maxsize + 1)
		return self.stack.pop()

	def peek(self):
		if self.is_empty():
			return float("-inf")
		return self.stack[-1]

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(50)

print stack.pop()
print stack.peek()
print stack.pop()