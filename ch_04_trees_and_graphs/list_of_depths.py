"""
PROBLEM

List of Depths: 
* Given a binary tree, design an algorithm which creates a linked list of all the nodes 
	at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 
"""

from typing import List

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

class ListNode:
	def __init__(self, x):
		self.data = x
		self.next = None


	def pretty_print(self):
		print(self.data, end='')
		node = self.next
		while(node):
			print(" -> %d" % node.data, end='')
			node = node.next
		print()

class Queue:
	def __init__(self):
		self.q = []

	def __len__(self):
		return len(self.q)

	def is_empty(self):
		return len(self) == 0

	def enqueue(self, x):
		self.q.append(x)

	def dequeue(self):
		if len(self) > 0:
			x = self.q[0]
			self.q = self.q[1:]
			return x
		else:
			print("Queue is empty. Dequeue operation cannot be performed.")
			return None	


"""
Notes:
* Use breadth-first search to construct the linked-list at each depth
"""
def list_of_depths(root : TreeNode) -> List[ListNode]:
	
	q = Queue()
	root.visited = True
	prev_d = -1
	d = 0
	q.enqueue((root, d))

	l_node = ListNode(root.data)
	l = [] 

	while(not q.is_empty()):

		node, d = q.dequeue()
		node.visited = True
		
		if prev_d < d:
			prev_d = d
			l_node = ListNode(node.data)
			l.append(l_node)
		else:
			l_node.next = ListNode(node.data)
			l_node = l_node.next


		if node.left:
			node.left.visited = True
			q.enqueue((node.left, d+1))

		if node.right:
			node.right.visited = True
			q.enqueue((node.right, d+1))


	return l




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
	node.right.right = TreeNode(11)

	for l_node in list_of_depths(node): l_node.pretty_print()
	print()

	node.unvisit()

	node.right = TreeNode(12)
	node.right.left = TreeNode(10)
	node.right.right = TreeNode(14)

	node.right.left.left = TreeNode(9)
	node.right.left.right = TreeNode(11)

	node.right.right.left = TreeNode(13)
	node.right.right.right = TreeNode(15)

	for l_node in list_of_depths(node): l_node.pretty_print()