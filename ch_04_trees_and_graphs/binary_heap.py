

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

"""
Notes:
* A min-heap is a complete binary tree which can also has its rightmost element filled at last level.
If this is the case, then insert() operation should add an extra node, increasing the depth by one.

"""

# def get_rightmost_node(node):
# 	n = node.node_count()
# 	d = node.depth()
# 	l = d

# 	if n != 2 ** d: # If binary heap is not a perfect binary tree

# 		r = 2 ** d - n - 1
# 		l = d - r 

# 		while(r > 0):
# 			node = node.right
# 			r -= 1

# 	while(l > 1):
# 		node = node.left
# 		l -= 1

# 	return node





def insert(data):
	node = MinHeapNode(data)
	pass



def extract_min():
	pass


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


	print(root.depth())
	print(root.node_count())

	print(get_rightmost_node(root).data)




