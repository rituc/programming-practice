from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def is_cyclic_util(self, v, visited, rec_stack):
		visited[v] = True
		rec_stack[v] = True

		for node in self.graph[v]:
			if visited[node] == False:
				if self.is_cyclic_util(node, visited, rec_stack) == True:
					return True
				elif rec_stack[node] == True:
					return True

		rec_stack[v] = False
		return False

	def is_cyclic(self):
		visited = [False]*self.V
		rec_stack = [False]*self.V

		for node in range(self.V):
			if visited[node] == False:
				if self.is_cyclic_util(node, visited, rec_stack):
					return True

		return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print "Cycle" if g.is_cyclic()== 1 else "No Cycle"

