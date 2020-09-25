"""
PROBLEM

Minimal Tree:
* Given a sorted (increasing order) array with unique integer elements, 
	write an algo­rithm to create a binary search tree with minimal height. 
"""

from typing import List
from math import log, floor

class TreeNode:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
		self.visited = False


"""
Notes:
* If the question did not ask the constructed BST to be minimal height, 
	then we could easily place each node as the left most one
	(resulting in a tree with maximal height).
* We can find the root. Given an array we can first extract 
	the data of the root and approach the problem recursively.

"""

def minimal_tree(l : List[int]) -> TreeNode:

	n = len(l)
	if n == 0:
		return None
	else:
		i = floor(log(n, 2))
		i = 2**i - 1
		
		root = TreeNode(l[i])
		root.left = minimal_tree(l[:i])
		root.right = minimal_tree(l[i+1:])
		return root


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

if __name__ == '__main__':

	print_tree(minimal_tree([1,2,3,4,5,6,7,8,9,10,11]), 4)
