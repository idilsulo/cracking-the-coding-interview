
# Tree
class TreeNode:
	def __init__(self, x):
		self.data = x
		self.children = None


# Binary tree
class BinaryTreeNode:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None


def depth(node):

	if node == None:
		return 0
	elif node.left and node.right:
		return 1 + (depth(node.left) if depth(node.left) > depth(node.right) else depth(node.right))
	elif node.left:
		return 1 + depth(node.left)
	else:
		return 1 + depth(node.right)


def node_count(node):

	if node == None:
		return 0
	elif not node.left and not node.right:
		return 1
	else:
		 return 1 + node_count(node.left) + node_count(node.right)


# Types of Binary Trees
####################################################################################################

"""
Binary search tree:

* A binary search tree is a binary tree in which every node fits a specific ordering property: 
	all left descendents <= n < all right descendents. 
* This must be true for each node n.
"""
def is_binary_search_tree(node):
	if (not node.right) and (not node.left):
		return True
	elif (not node.right):
		if node.left.data > node.data:
			return False
		else:
			return is_binary_search_tree(node.left)
	elif (not node.left):
		if node.right.data <= node.data:
			return False
		else:
			return is_binary_search_tree(node.right)
	else:
		if (node.right.data <= node.data) or (node.left.data > node.data):
			return False
		else:
			return is_binary_search_tree(node.left) and is_binary_search_tree(node.right)


"""
Complete binary tree:

* A complete binary tree is a binary tree in which every level of the tree is fully filled, 
except for perhaps the last level. 
* To the extent that the last level is filled, it is filled left to right. 

Notes:
* Very neat solution for checking if the binary tree is complete
* Keep the index and node count while traversing the tree (giving priority to the left child).
* If the index ever exceeds the node count then three is incomplete.

"""
def index_and_node_number_check(node, index, no_nodes):

	if node == None:
		return True

	if index >= no_nodes:
		return False

	return index_and_node_number_check(node.left, 2*index+1, no_nodes) and \
			index_and_node_number_check(node.right, 2*index+2, no_nodes)


def is_complete_binary_tree(node):

	no_nodes = node_count(node)

	return index_and_node_number_check(node, 0, no_nodes)


"""
Full binary tree:

* A full binary tree is a binary tree in which every node has either zero or two children. 
* That is, no nodes have only one child.
"""
def is_full_binary_tree(node):

	if (not node.right) and (not node.left):
		return True
	elif (not node.left) and (node.right):
		return False
	elif (node.left) and (not node.right):
		return False
	else:
		return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)

"""
Perfect binary tree:

* Perfect Binary Trees A perfect binary tree is one that is both full and complete. 
* All leaf nodes will be at the same level, and this level has the maximum number of nodes. 
"""
def is_perfect_binary_tree(node):
	return is_full_binary_tree(node) and is_complete_binary_tree(node)


# Binary Tree Traversal
####################################################################################################

"""
In-Order Traversal:

* In-order traversal means to "visit" (often, print) the left branch, then the current node, 
	and finally, the right branch. 
* When performed on a binary search tree, it visits the nodes in ascending order 
	(hence the name "in-order"). 
"""

def in_order_traversal(node):

	if(node != None):
		in_order_traversal(node.left)
		print("| %d | " % (node.data), end='')
		in_order_traversal(node.right)

"""
Pre-Order Traversal:

* Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").
* In a pre-order traversal, the root is always the first node visited. 

Notes:
* If we store the nodes visited by pre-order traversal in an array, for a k-th element 
	of the array:
	- Left child is located at 2*k index
	- Right child is located at 2*k+1 index
	- Parent is located at k/2 index
	
"""
def pre_order_traversal(node):

	if(node != None):
		print("| %d | " % (node.data), end='')
		pre_order_traversal(node.left)
		pre_order_traversal(node.right)

"""
Post-Order Traversal

* Post-order traversal visits the current node after its child nodes (hence the name "post-order").
* In a post-order traversal, the root is always the last node visited.
"""
def post_order_traversal(node):

	if(node != None):
		post_order_traversal(node.left)
		post_order_traversal(node.right)
		print("| %d | " % (node.data), end='')


if __name__ == '__main__':
	root = BinaryTreeNode(8)
	root.left = BinaryTreeNode(6)
	root.right = BinaryTreeNode(10)

	root.left.left = BinaryTreeNode(4)
	root.left.right = BinaryTreeNode(7)

	print("Is binary search tree: ", is_binary_search_tree(root))

	root.right.right = BinaryTreeNode(1)
	root.right.left = None
	print("Is binary search tree: ", is_binary_search_tree(root))
	print("Is complete binary tree: ", is_complete_binary_tree(root))

	root.right.left = BinaryTreeNode(1)
	root.right.right = None

	print("Is complete binary tree: ", is_complete_binary_tree(root))
	print("Is full binary tree: ", is_full_binary_tree(root))
	print("Depth of tree: ", depth(root))
	print("# of nodes in tree: ", node_count(root))

	root.right.left = None
	print("# of nodes in tree: ", node_count(root))
	print("Is complete binary tree: ", is_complete_binary_tree(root))

	print("In-order traversal: ")
	in_order_traversal(root)
	print()

	print("Pre-order traversal: ")
	pre_order_traversal(root)
	print()

	print("Post-order traversal: ")
	post_order_traversal(root)
	print()

