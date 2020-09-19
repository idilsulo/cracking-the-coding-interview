"""
Graphs are a generalized version of trees which implies that not all graphs are necessarily trees. 
Yet, all trees are graphs. In fact, they are a connected graph without any cycles.
"""

# Graph Representation
####################################################################################################
"""
Graphs can be represented in two ways:
	* Adjacency list:   Mostly preferred for sparse graph representations
	* Adjacency matrix: Mostly preferred for dense graph representations
"""
class GraphNode:
	def __init__(self, x):
		self.val = x
		self.adjacents = []		 # Nodes n where there is a directed edge from this node to n
		self.visited = False	 # Used in depth-first and breadth-first search

	def neighbors(self):
		return self.adjacents

class Graph:
	def __init__(self):
		self.nodes = None

"""
Notes:
* If you are in between representations and cannot decide, here is a link to help you: 
	https://cs.stackexchange.com/questions/79322/when-are-adjacency-lists-or-matrices-the-better-choice
"""
# Adjacency matrix representation
class GraphM(Graph):
	def __init__(self, max_nodes=10):
		super().__init__()
		self.nodes = [[0] * max_nodes] * max_nodes

	def add_edge(self, node1, node2):
		self.nodes[node1][node2] = 1

	def delete_edge(self, node1, node2):
		self.nodes[node1][node2] = 0

	# Iterates through all the nodes to identify node's neighbors
	def neighbors(self, node):
		neighbors = []
		for i, edge in enumerate(self.nodes[node]):
			if edge == 1: neighbors.append(i)

		return neighbors

# Adjacency list representation
class GraphL(Graph):
	def __init__(self):
		super().__init__()
		self.nodes = []

	def add_node(self, node):
		self.nodes.append(node)

	def add_edge(self, node1, node2):
		i = self.nodes.index(node1)
		self.nodes[i].adjacents.append(node2)

	def delete_node(self, node):
		i = self.nodes.index(node)
		for adj in adjacents:
			if node in adj.adjacents:
				adj.adjacents.remove(node)

	def delete_edge(self, node1, node2):
		i = self.nodes.index(node1)
		self.nodes[i].adjacents.remove(node2)

	def pretty_print(self):
		
		for node in self.nodes:
			print(node.val, end=' :')
			if len(node.adjacents) > 0: print(' %d' % node.adjacents[0].val, end='')
			for adj in node.adjacents[1:]:
				print(' , %d' % adj.val, end='')
			print()

	def unvisit(self):
		for node in self.nodes:
			node.visited = False
			if len(node.adjacents) > 0: node.adjacents[0].visited = False
			for adj in node.adjacents[1:]:
				adj.visited = False

# Graph Search
####################################################################################################

"""
There are two most common ways to search a graph:
* Depth-first search (DFS)
* Breadth-first search (BFS)

"""

"""
Depth-first search (DFS):
* Explore each branch completely before moving on to the next branch
"""
def depth_first_search(node):
	if len(node.adjacents) == 0 and not node.visited: 
		node.visited = True
		print(node.val, end=' ')
	else:
		node.visited = True
		print(node.val, end=' ')
		for n in node.adjacents:
			if not n.visited: depth_first_search(n)


class Queue:
	def __init__(self):
		self.queue = []

	def __len__(self):
		return len(self.queue)

	def enqueue(self, x):
		self.queue.append(x)

	def dequeue(self):
		x = self.queue[0]
		self.queue = self.queue[1:]
		return x

"""
Breadth-first search (BFS):
* Explore each neighbor before going on to any of their children
"""
def breadth_first_search(node):
	q = Queue()
	node.visited = True
	print(node.val, end=' ')

	q.enqueue(node)

	while(len(q) > 0):
		n = q.dequeue()
		for adj in n.adjacents:
			if not adj.visited:
				adj.visited = True
				print(adj.val, end=' ')
				q.enqueue(adj)


# TO-DO: Bi-directional search


if __name__ == '__main__':

	# Adjacency matrix representation
	_g = GraphM()
	_g.add_edge(1, 2)
	_g.add_edge(2, 2)
	_g.add_edge(3, 2)

	print("Neighbors of %d: %s" % (2, str(_g.neighbors(2))))
	print(_g.nodes)

	# Adjacency list representation
	g = GraphL()

	n1 = GraphNode(1)
	n2 = GraphNode(2)
	n3 = GraphNode(3)
	n4 = GraphNode(4)
	n5 = GraphNode(5)
	n6 = GraphNode(6)

	g.add_node(n1)
	g.add_node(n2)
	g.add_node(n3)
	g.add_node(n4)
	g.add_node(n5)
	g.add_node(n6)

	g.add_edge(n1,n2)
	g.add_edge(n1,n3)
	g.add_edge(n3,n2)
	g.add_edge(n2,n4)
	g.add_edge(n5,n6)
	g.add_edge(n5,n4)
	g.add_edge(n4,n3)
	g.add_edge(n3,n5)

	g.pretty_print()

	print("Depth-first search: ")
	depth_first_search(n1)
	print()

	g.unvisit()

	print("Breadth-first search: ")
	breadth_first_search(n1)
	print()

	g.unvisit()







