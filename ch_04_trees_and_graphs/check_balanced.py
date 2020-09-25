"""
PROBLEM

Check Balanced: 
* Implement a function to check if a binary tree is balanced. 
* For the purposes of this question, a balanced tree is defined to be a tree such that 
	the heights of the two subtrees of any node never differ by more than one. 
"""

class TreeNode:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
		self.visited = False

	def unvisit(self):
		self.visited = False
		if self.left: self.left.unvisit()
		if self.right: self.right.unvisit()


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

def print_tree(node, depth):
	q = Queue()
	node.visited = True
	print(node.data)

	d = depth
	prev_d = depth
	q.enqueue((node, d))

	while(len(q) > 0):
		n, d = q.dequeue()
		if d < prev_d:
			prev_d = d
			print()

		# print('\t'*(d), end='')
		if n.left:
			if not n.left.visited:
				n.left.visited = True
				print(n.left.data, end=' ')
				q.enqueue((n.left, d-1))
		# print('\t'*(d), end='')
		if n.right:
			if not n.right.visited:
				n.right.visited = True
				print(n.right.data, end=' ')
				q.enqueue((n.right, d-1))

		d -= 1

def min_depth(node : TreeNode, d : int) -> int:

	if not node:
		return d
	else:
		l = min_depth(node.left, d+1)
		r = min_depth(node.right, d+1)
		return min(l,r)

def max_depth(node : TreeNode, d : int) -> int:
	if not node:
		return d
	else:
		l = max_depth(node.left, d+1)
		r = max_depth(node.right, d+1)
		return max(l,r)

def check_balanced(node : TreeNode) -> bool:
	minimum = min_depth(node, 0)
	maximum = max_depth(node, 0)
	print_tree(node, maximum)
	return True if maximum-minimum < 2 else False


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

	print("Is balanced BST? %r" % check_balanced(node))
	
	node.unvisit()
	node.right.right = TreeNode(11)

	print("Is balanced BST? %r" % check_balanced(node))

	node.unvisit()
	node.right = TreeNode(12)
	node.right.left = TreeNode(10)
	node.right.right = TreeNode(14)

	node.right.left.left = TreeNode(9)
	node.right.left.right = TreeNode(11)

	node.right.right.left = TreeNode(13)
	node.right.right.right = TreeNode(15)

	print("Is balanced BST? %r" % check_balanced(node))
	