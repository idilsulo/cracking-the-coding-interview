

"""
Min Heap:

* A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last level) 
where each node is smaller than its children. The root, therefore, is the minimum element in the tree. 

* Max-heaps are essentially equivalent to Min-heaps, but the elements are in descending order rather than ascending order. 
"""

class MinHeapNode:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
		self.parent = None
		self.visited = False

	"""
	Notes:
	* As binary heaps are a specific type of complete binary tress, we can go to the leftmost node for calculating depth.
	* This depth computation is only suitable in such a case, and it still has O(N) time complexity. As in the worst case,
		the nodes might be sequentially ordered.

	"""
	def depth(self):
		d = 1
		l = self.left
		while(l):
			l = l.left
			d += 1

		return d



	def node_count(self):

		if not self.left and not self.right:
			return 1
		elif not self.left:
			return 1 + self.right.node_count()
		elif not self.right:
			return 1 + self.left.node_count()
		else:
			 return 1 + self.left.node_count() + self.right.node_count()

def breadth_first_search(s, l, show=False): 


	# Create a queue for BFS 
	queue = [] 

	# Mark the source node as visited and enqueue it 
	if s and not s.visited:
		queue.append(s) 
		s.visited = True

	while queue: 

		# Dequeue a vertex from queue and print it 
		s = queue.pop(0) 

		# Mark the popped node as not-visited again, 
		# so that the tree can again be used for breadth-first search
		s.visited = False

		if show:
			print(s.data, end = " ") 
		l.append(s.data)


		# Get all adjacent vertices of the dequeued vertex s. 
		# If an adjacent has not been visited, then mark it visited and enqueue it 
		if s.left and not s.left.visited:
			queue.append(s.left)
			s.left.visited = True
			breadth_first_search(s.left, l)
		if s.right and not s.right.visited:
			queue.append(s.right)
			s.right.visited = True
			breadth_first_search(s.right,l)

	return l

def print_tree(root):

	l = breadth_first_search(root, [])

	i, j = 0, 1
	d = 2**j-1
	n = len(l)

	if l:
		while(i < n):
			while(i < d and i < n):
				print(l[i], end=' ')
				i += 1
			j += 1
			d = 2**j-1
			print()

"""
Notes:
* A min-heap is a complete binary tree which can also has its rightmost element filled at last level.
If this is the case, then insert() operation should add an extra node, increasing the depth by one.

"""
def get_available_pos(node, index):
	if not node:
		return (None, index)
	elif (not node.left and not node.right) or (not node.right):
		return (node, index)
	else:
		l, l_index = get_available_pos(node.left, 2*index+1)
		r, r_index = get_available_pos(node.right, 2*index+2)
		
		return (l, l_index) if l_index < r_index else (r, r_index)


	
def swap(node1, node2, left=True):

	root_update = node1.parent == None

	if node1.parent:
		if node1.parent.left == node1:
			node1.parent.left = node2
		else:
			node1.parent.right = node2
	
	node2.parent = node1.parent
	
	l = node2.left
	r = node2.right

	if left:
		node2.right = node1.right
		node2.left = node1
	else:
		node2.left = node1.left
		node2.right = node1	

	node1.left = l
	node1.right = r
	node1.parent = node2

	return root_update
	

"""
* Time Complexity: Takes O(logn) time, where n is the number of nodes in the heap.
"""
def insert(root, data):

	node = MinHeapNode(data)
	parent, _ = get_available_pos(root, 0)
	left = False

	if(parent and node.data < parent.data):
		while(parent and node.data < parent.data):

			if not parent.left:
				left = True
				parent.left = node
			else:
				parent.right = node

			node.parent = parent

			if swap(parent, node, left):
				root = node
			parent = node.parent
	else: # No swapping needed, insert the element to the lowest level
		if not parent.left:
			parent.left = node
		else:
			parent.right = node

	return root

def get_rightmost_bottommost(node, d):
	if not node:
		return (None, d)
	elif not node.left and not node.right:
		return (node, d)
	elif not node.right:
		return get_rightmost_bottommost(node.left, d+1)
	elif not node.left:
		return get_rightmost_bottommost(node.left, d+1)
	else:
		l, l_index = get_rightmost_bottommost(node.left, d+1)
		r, r_index = get_rightmost_bottommost(node.right, d+1)
		return (l, l_index) if l_index > r_index else (r, r_index)



def extract_min(root):
	val = root.data
	node, _ = get_rightmost_bottommost(root, 0)
	
	if node.parent.left == node:
		node.parent.left = None
	else:
		node.parent.right = None
	
	node.right = root.right
	node.left = root.left
	node.parent = None

	flag = True

	while(node.left or node.right):
		
		if node.left:
			l = node.left.data
			if node.right:
				r = node.right.data
				if r < l:
					tmp = node.right
					swap(node, tmp, False)
			else:
				tmp = node.left
				swap(node, tmp, True)
		else:
			tmp = node.right
			swap(node, tmp, False)


		if flag:
			flag = False
			root = tmp


	return root




if __name__ == '__main__':

	root = MinHeapNode(4)
	root.left = MinHeapNode(50)
	root.left.parent = root
	root.right = MinHeapNode(7)
	root.right.parent = root
	root.left.left = MinHeapNode(55)
	root.left.left.parent = root.left
	root.left.right = MinHeapNode(90)
	root.left.right.parent = root.left
	root.right.left = MinHeapNode(87)
	root.right.left.parent = root.right


	print("Depth: ",root.depth())
	print("Node count: ", root.node_count())

	print("Printing tree:")
	print_tree(root)

	root = insert(root, 2)

	
	print("Printing tree:")
	print_tree(root)

	root = insert(root, 80)
	print("Printing tree:")
	print_tree(root)

	print()
	print("New test case")

	root = MinHeapNode(4)
	root.left = MinHeapNode(50)
	root.left.parent = root
	root.right = MinHeapNode(23)
	root.right.parent = root
	root.left.left = MinHeapNode(88)
	root.left.left.parent = root.left
	root.left.right = MinHeapNode(90)
	root.left.right.parent = root.left
	root.right.left = MinHeapNode(32)
	root.right.left.parent = root.right
	root.right.right = MinHeapNode(74)
	root.right.right.parent = root.right

	print("Printing tree:")
	print_tree(root)

	print("extract_min()")
	root = extract_min(root)

	print("Printing tree:")
	print_tree(root)
