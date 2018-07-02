from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs_util(self, v, visited):
		visited[v] = True
		print v,

		for i in self.graph[v]:
			if visited[i] == False:
				self.dfs_util(i, visited)


	def dfs(self):
		V = len(self.graph)
		visited = [False]*(V)

		for i in range(V):
			if visited[i] == False:
				self.dfs_util(i, visited)


def main():
	g = Graph()
	# g.add_edge(0,1)
	# g.add_edge(0,2)
	# g.add_edge(1,2)
	# g.add_edge(2,0)

	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	g.dfs()

if __name__ == '__main__':
	main()