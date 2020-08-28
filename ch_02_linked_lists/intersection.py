"""
PROBLEM

Intersection: 
* Given two (singly) linked lists, determine if the two lists intersect. 
* Return the inter­secting node. Note that the intersection is defined based on reference, not value. 
* That is, if the kth node of the first linked list is the exact same node (by reference) as the 
	jth node of the second linked list, then they are intersecting.
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


"""
Notes:
* A linked-list node cannot point totwo different nodes as its next node
* If they ever intersect, they need to have their last node as the exact same node 

* Time Complexity: O(N), ~O(2*N), where N grows with input size
* Space Complexity: O(1), no additional space required

"""
def intersection(l1 : ListNode, l2: ListNode) -> bool:
	
	while(l1.next):
		l1 = l1.next 

	while(l2.next):
		l2 = l2.next

	return l1 == l2




if __name__ == '__main__':

	node = ListNode(7)
	head1 = node
	intersect =  ListNode(1)
	node.next = intersect
	node = node.next
	node.next = ListNode(6)

	node = ListNode(5)
	head2 = node
	node.next = ListNode(9)
	node = node.next
	node.next = intersect

	pretty_print(head1)
	pretty_print(head2)

	print("TEST CASE #1 : %r" % (intersection(head1, head2)))

