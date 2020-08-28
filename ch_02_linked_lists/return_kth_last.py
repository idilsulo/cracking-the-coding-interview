"""
PROBLEM

Return Kth to Last: 
* Implement an algorithm to find the kth to last element of a singly linked list.
"""

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

def kth_to_last(l : ListNode, k : int) -> ListNode:
	
	head = l
	cnt = count_nodes(head)

	i = 0
	while(i < cnt - k):
		l = l.next
		i += 1

	return l



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

	pretty_print(kth_to_last(head, 3))

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

	pretty_print(kth_to_last(head, 5))

