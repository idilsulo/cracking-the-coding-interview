"""
PROBLEM

Loop Detection: 
* Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. 

DEFINITION 
* Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, 
	so as to make a loop in the linked list. 

EXAMPLE 
* Input: A  ->  B  ->  C  ->  D  ->  E  ->  C [the same C as earlier] 
* Output: C 

"""


"""
Notes: 
* If modifying the definition of the data structure is allowed,
	the nodes that had been previously visited can be marked with a flag.

* Time Complexity: O(N)
* Space Complexity: O(1)

"""
class ListNode:
	def __init__(self, x):
		self.visited = False
		self.val = x
		self.next = None



def loop_detection(l : ListNode) -> ListNode:
	while(l.next):
		if not l.visited:
			l.visited = True
			l = l.next
		else:
			return l


if __name__ == '__main__':
	node = ListNode(7)
	head = node
	corrupt =  ListNode(1)
	node.next = corrupt
	node = node.next
	node.next = ListNode(6)
	node = node.next
	node.next = corrupt

	print("TEST CASE #1 - Corrupt Node: %d" % (loop_detection(head).val))

	node = ListNode(7)
	head = node
	corrupt =  ListNode(1)
	node.next = corrupt
	node = node.next
	node.next = ListNode(6)
	node = node.next
	node.next = corrupt
	node.next = ListNode(3)
	node = node.next
	node.next = corrupt

	print("TEST CASE #2 - Corrupt Node: %d" % (loop_detection(head).val))
