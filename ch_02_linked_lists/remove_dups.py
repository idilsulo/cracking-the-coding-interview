"""
PROBLEM

Remove Dups:
* Write code to remove duplicates from an unsorted linked list.
* FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
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
This approach only works on sorted linked lists.

* Time Complexity: O(N), N length of linked-list
* Space Complexity: O(1), no temporary buffer
"""
def remove_dups(l : ListNode) -> ListNode:
	
	prev = l
	head = l
	l = l.next
	while(l):
		if prev.val == l.val:
			prev.next = l.next
			l = l.next
		else:
			prev = prev.next
			l = l.next
	return head


"""
TO-DO: Work on the general case where duplicates can occur in any order
"""



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

	pretty_print(remove_dups(head))
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

	pretty_print(remove_dups(head))