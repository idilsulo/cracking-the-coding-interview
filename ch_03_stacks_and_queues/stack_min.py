"""
PROBLEM

Stack Min: 
* How would you design a stack which, in addition to push and pop, 
	has a function min which returns the minimum element? 
* Push, pop and min should all operate in 0(1) time. 
"""

"""
Notes:
* This question is really good.

* Consider having each node know the minimum of  its "substack" 
	(all  the elements beneath it, including itself).
* If all the nodes know the minimum in its substack, access time to the minimum
	element is O(1).
* On top of the default pop() and push() operations, we need to check if we have 
	a new global minimum, and update it accordingly. 
* These checks also require O(1) time, so the time complexity of pop(), push()
	and minimum() is O(1).


"""

class StackNode:
	def __init__(self, x):
		self.data = x
		self.next = None
		self.min_node = self

class Stack:
	def __init__(self):
		self.top = None
		self.min = None
		self.count = 0


	def pop(self):

		if self.count == 0:
			print("Stack is empty.")
		elif self.count == 1:
			self.min = None
			self.top = None
			self.count = 0
		else:
			self.min = self.top.next.min_node
			self.top = self.top.next
			self.count -= 1


	def push(self, item):

		node = StackNode(item)
		node.next = self.top
		self.top = node
		self.count += 1

		if self.count == 1:
			self.min = node
		else:
			node.min_node = self.min
			if self.minimum() > item:
				self.min = node


	def peek(self):
		if self.count > 0:
			return self.top.data
		return None


	def is_empty(self):
		return self.count == 0


	def minimum(self):
		if self.count > 0:
			return self.min.data
		else:
			print("Stack is empty.")
			return None




if __name__ == '__main__':

	s = Stack()

	s.push(1)
	s.push(2)
	s.push(0)
	s.push(3)

	print("Count: %d" % (s.count))
	print("Min  : %d" % (s.minimum()))

	s.pop()

	print("Count: %d" % (s.count))
	print("Min  : %d" % (s.minimum()))

	s.pop()

	print("Count: %d" % (s.count))
	print("Min  : %d" % (s.minimum()))




