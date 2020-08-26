"""
PROBLEM

Sum Lists: 
* You have two numbers represented by a linked list, where each node contains a single digit. 
* The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
* Write a function that adds the two numbers and returns the sum as a linked list. 

EXAMPLE 
* Input: (7-> 1  -> 6)  + (5  ->  9  ->  2). That is, 617 +  295. 
* Output: 2  ->  1 ->  9. That is, 912. 

FOLLOW UP 
* Suppose the digits are stored in forward order. 
* Repeat the above problem. 

EXAMPLE 
* Input:(6  ->  1  ->  7)  + (2  ->  9  ->  5). That is, 617 +  295. 
* Output: 9  ->  1 ->  2. That is, 912.
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


"""
* Time Complexity: O(N), N: # of nodes in linked-list
* Space Complexity: O(N), N: linked-list storing the result, grows with input size

"""
def sum_lists(l1 : ListNode, l2: ListNode) -> ListNode:

	digit = 0
	carry = 0

	node = None
	head = None
	temp = None

	while(l1 or l2):

		if(l1 and l2):
			digit = l1.val + l2.val + carry
			carry = floor(digit / 10)
			digit = digit % 10

			l1 = l1.next
			l2 = l2.next
		
		elif(l1):
			digit = l1.val + carry
			carry = floor(digit / 10)
			digit = digit % 10

			l1 = l1.next

		else:
			digit = l2.val + carry
			carry = floor(digit / 10)
			digit = digit % 10

			l2 = l2.next

		node = ListNode(digit)

		if not head:
			head = node
			temp = node
		else:		
			temp.next = node
			temp = temp.next

	return head

"""
TO-DO: Second part, consider the linked-lists in reverse order
"""

if __name__ == '__main__':

	node = ListNode(7)
	head1 = node
	node.next = ListNode(1)
	node = node.next
	node.next = ListNode(6)

	node = ListNode(5)
	head2 = node
	node.next = ListNode(9)
	node = node.next
	node.next = ListNode(2)

	pretty_print(head1)
	pretty_print(head2)
	pretty_print(sum_lists(head1, head2))




	