import networkx as nx
import pylab as plt


class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

	# Function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(i + 1, "-", parent[i] + 1, "\t", self.graph[i][parent[i]])

	def drawMST(self, parent):
		self.g = nx.DiGraph()
		self.listing = []
		self.old_edges = []
		for i in range(1, self.V + 1):
			for j in range(1, self.V + 1):
				self.old_edges.append((i, j))
		for i in range(1, self.V):
			self.g.add_node(i + 1)
			self.g.add_edge(i + 1, parent[i] + 1)
			self.listing.append((i + 1, parent[i] + 1))
		nx.draw(self.g, pos=nx.shell_layout(self.g), with_labels=True, font_weight='bold')
		nx.draw_networkx_edges(self.g, pos=nx.shell_layout(self.g), edgelist=self.old_edges, edge_color='b',
			with_labels=True)
		nx.draw_networkx_edges(self.g, pos=nx.shell_layout(self.g), edgelist=self.listing, edge_color='r',
			with_labels=True)
		plt.show()
	def minKey(self, key, mstSet):
		# Initilaize min value
		min = 1000000
		for v in range(self.V):
			if key[v] < min and mstSet[v]==False:
				min = key[v]
				min_index = v
		return min_index

	def primMST(self):
		key = [1000000] * self.V
		parent = [None] * self.V
		key[0] = 0
		mstSet = [False] * self.V
		parent[0] = -1
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v]==False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u
		self.printMST(parent)
		self.drawMST(parent)

if __name__ == "__main__":
	g = Graph(5)
	g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0],
           ]
	g.primMST()
