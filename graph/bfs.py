from collections import defaultdict

class Graph:

	# Constructor
	def __init__(self):
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def add_edge(self, u, v):
		self.graph[u].append(v)

	def bfs(self, s):
		# Mark all the vertices as not visited
		print len(self.graph)
		visited = [False]*len(self.graph)
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop(0)
			print s,

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


def main():
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	g.bfs(3)

if __name__ == '__main__':
	main()



