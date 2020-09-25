"""
PROBLEM

Validate BST:
* Implement a function to check if a binary tree is a binary search tree.
"""

class TreeNode:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None


def validate_bst(node :  TreeNode) -> bool:
	if (not node.right) and (not node.left):
		return True
	elif (not node.right):
		if node.left.data > node.data:
			return False
		else:
			return validate_bst(node.left)
	elif (not node.left):
		if node.right.data <= node.data:
			return False
		else:
			return validate_bst(node.right)
	else:
		if (node.right.data <= node.data) or (node.left.data > node.data):
			return False
		else:
			return validate_bst(node.left) and validate_bst(node.right)

if __name__ == '__main__':

	node = TreeNode(8)
	node.left = TreeNode(4)
	node.right = TreeNode(10)

	node.left.left = TreeNode(2)
	node.left.right = TreeNode(6)

	node.left.left.left = TreeNode(1)
	node.left.left.right = TreeNode(3)

	node.left.right.left = TreeNode(5)
	node.left.right.right = TreeNode(7)

	node.right.left = TreeNode(9)

	print("Is valid BST? %r" % validate_bst(node))
	
	# node.unvisit()
	node.right.right = TreeNode(11)

	print("Is valid BST? %r" % validate_bst(node))

	# node.unvisit()
	node.right = TreeNode(12)
	node.right.left = TreeNode(10)
	node.right.right = TreeNode(14)

	node.right.left.left = TreeNode(9)
	node.right.left.right = TreeNode(11)

	node.right.right.left = TreeNode(13)
	node.right.right.right = TreeNode(15)

	print("Is valid BST? %r" % validate_bst(node))
	
	node.right.right.right = TreeNode(10)

	print("Is valid BST? %r" % validate_bst(node))
