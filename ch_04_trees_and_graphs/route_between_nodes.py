"""
PROBLEM

Route Between Nodes: 
* Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

class GraphNode:
	def __init__(self, x):
		self.val = x
		self.adjacents = []
		self.visited = False

class Graph:
	def __init__(self):
		self.nodes = []

	def add_node(self, node):
		self.nodes.append(node)

	def add_edge(self, node1, node2):
		node1.adjacents.append(node2)

	def delete_node(self, node):
		i = self.nodes.index(node)
		for adj in adjacents:
			if node in adj.adjacents:
				adj.adjacents.remove(node)

	def delete_edge(self, node1, node2):
		node1.adjacents.remove(node2)

	def pretty_print(self):
		
		for node in self.nodes:
			print(node.val, end=' :')
			if len(node.adjacents) > 0: print(' %d' % node.adjacents[0].val, end='')
			for adj in node.adjacents[1:]:
				print(', %d' % adj.val, end='')
			print()
		print()

	def unvisit(self):
		for node in self.nodes:
			node.visited = False
			if len(node.adjacents) > 0: node.adjacents[0].visited = False
			for adj in node.adjacents[1:]:
				adj.visited = False


	"""
	Notes:
	* In order to find if there is a route between the nodes select one of the nodes 
		as the source and the other as the target, and search. If the graph is directed, 
		then it might be necessary to search once more choosing the node which was 
		previously selected as target as the source node.
	* The search operation can be performed via DFS or BFS.
	"""

	# Depth-first Search (DFS)
	def search(self, node, target):
		if len(node.adjacents) == 0: 
			print(node.val)
			node.visited = True
			if node == target: 
				return True
			else:
				return False
		else:
			print(node.val)
			node.visited = True
			if node == target: 
				return True
			for n in node.adjacents:
				if not n.visited:
					if self.search(n, target):
						return True

			return False

	def route_between_nodes(self, node1, node2):
		# If first search returns True, second search is not performed

		if g.search(node1, node2):
			return True
		else:
			g.unvisit()
			print()
			return g.search(node2, node1)
	


if __name__ == '__main__':

	g = Graph()

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

	# g.add_edge(n1,n2)
	g.add_edge(n1,n3)
	g.add_edge(n3,n2)
	g.add_edge(n2,n4)
	g.add_edge(n5,n6)
	g.add_edge(n5,n4)
	g.add_edge(n4,n3)
	# g.add_edge(n3,n5)

	g.pretty_print()

	print("Is there a route between node #%d and node #%d? %r" % (n1.val, n5.val, g.route_between_nodes(n1,n5)))
	g.unvisit()

	print("Is there a route between node #%d and node #%d? %r" % (n2.val, n3.val, g.route_between_nodes(n2,n3)))
	g.unvisit()

	print("Is there a route between node #%d and node #%d? %r" % (n3.val, n4.val, g.route_between_nodes(n3,n4)))
	g.unvisit()

	print("Is there a route between node #%d and node #%d? %r" % (n2.val, n6.val, g.route_between_nodes(n2,n6)))
	g.unvisit()



