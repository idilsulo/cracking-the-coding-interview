"""
PROBLEM

Successor: 
* Write an algorithm to find the "next" node (i.e., in-order successor) 
	of a given node in a binary search tree. 
* You may assume that each node has a link to its parent. 
"""

class TreeNode:
	def __init__(self, x, parent=None):
		self.data = x
		self.left = None
		self.right = None
		self.parent = parent
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


def left_child(node : TreeNode):
	if node:
		while node.left:
			node = node.left
		return node
	else:
		return None

def successor(node : TreeNode) -> TreeNode:
	if node.right:
		return left_child(node.right)
	else:
		while node.parent and (node == node.parent.right):
			node = node.parent
		return node.parent


if  __name__ == '__main__':
	node = TreeNode(8)
	node.left = TreeNode(4)
	node.left.parent = node
	node.right = TreeNode(10)
	node.right.parent = node

	node.left.left = TreeNode(2)
	node.left.left.parent = node.left
	node.left.right = TreeNode(6)
	node.left.right.parent = node.left

	node.left.left.left = TreeNode(1)
	node.left.left.left.parent = node.left.left
	node.left.left.right = TreeNode(3)
	node.left.left.right.parent = node.left.left

	node.left.right.left = TreeNode(5)
	node.left.right.left.parent = node.left.right
	node.left.right.right = TreeNode(7)
	node.left.right.right.parent = node.left.right

	node.right.left = TreeNode(9)
	node.right.left.parent = node.right
	node.right.right = TreeNode(11)
	node.right.right.parent = node.right

	print_tree(node,3)
	print("Successor %d %d" % (node.left.right.right.data, successor(node.left.right.right).data))
	
	node.unvisit()
	
	print_tree(node,3)
	print("Successor %d %d" % (node.left.data, successor(node.left).data))



