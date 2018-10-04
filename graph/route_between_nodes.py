from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def check_path(self, s, node):
		visited = [False]*len(self.graph)
		visited[s] = True
		queue = []
		queue.append(s)
		while queue:
			s = queue.pop()
			for i in self.graph[s]:
				if not visited[i]:
					if i==node:
						return True
					else:
						visited[i] = True
		return False

g = Graph()
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print g.check_path(0, 1)

