class Minstack:

	def __init__(self):
		self.q = []

	def push(self, x):
		curr_min = self.get_min()

		if curr_min == None or x < curr_min:
			curr_min = x
		self.q.append((x, curr_min))

	def pop(self):
		self.q.pop()

	def top(self):
		return self.q[len(self.q)-1][0] if len(self.q) != 0 else None

	def get_min(self):
		return self.q[len(self.q)-1][1] if len(self.q) != 0 else None



