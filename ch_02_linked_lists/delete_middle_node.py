"""
PROBLEM

Delete Middle Node: 
* Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) 
	of a singly linked list, given only access to that node. 
"""

from math import floor


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def pretty_print(l : ListNode):

	while(l.next):
		print("%d -> " % (l.val), end='')
		l = l.next

	print(l.val)


def count_nodes(l : ListNode) -> int:

	if not l.next:
		return 1
	else:
		return 1 + count_nodes(l.next)


def delete_middle(l : ListNode):

	head = l
	tmp = l
	cnt = count_nodes(tmp)
	
	if cnt > 2: # Do not delete the first and last node
		cnt = floor(cnt / 2)

		prev = l
		i = 0
		while(i < cnt):
			prev = l
			l = l.next
			i += 1

		# l is the node to be deleted
		prev.next = l.next
		del l

	




if __name__ == '__main__':

	node = ListNode(1)
	head = node
	node.next = ListNode(2)
	node = node.next
	node.next = ListNode(2)
	node = node.next
	node.next = ListNode(3)
	node = node.next
	node.next = ListNode(4)

	delete_middle(head)
	pretty_print(head)

	del head

	node = ListNode(1)
	head = node
	node.next = ListNode(2)
	node = node.next
	node.next = ListNode(2)
	node = node.next
	node.next = ListNode(3)
	node = node.next
	node.next = ListNode(4)
	node = node.next
	node.next = ListNode(4)
	node = node.next
	node.next = ListNode(4)
	node = node.next
	node.next = ListNode(4)

	delete_middle(head)
	pretty_print(head)

