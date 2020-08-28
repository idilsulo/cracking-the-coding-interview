"""
PROBLEM

Queue via Stacks: 
* Implement a MyQueue class which implements a queue using two stacks. 
"""

class StackNode:
	def __init__(self, x):
		self.data = x
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self, item):
		node = StackNode(item)
		node.next = self.top
		self.top = node

	def pop(self):
		self.top = self.top.next

	def is_empty(self):
		return self.top == None

	def peek(self):
		return self.top.data


class MyQueue:
	def __init__(self):
		self.s = Stack()
		self.s_reverse = Stack()

	"""
	* Time Complexity: O(1)
	"""
	def enqueue(self, item):
		self.s.push(item)

	"""
	* Time Complexity: O(N), N grows with the # of nodes
	"""
	def dequeue(self):

		while(not self.s.is_empty()):
			self.s_reverse.push(self.s.peek())
			self.s.pop()
		
		print("Popping item: #%d" % (self.s_reverse.peek()))
		self.s_reverse.pop()

		while(not self.s_reverse.is_empty()):
			self.s.push(self.s_reverse.peek())
			self.s_reverse.pop()


	def print(self):
		while(not self.s.is_empty()):
			self.s_reverse.push(self.s.peek())
			self.s.pop()
		

		while(not self.s_reverse.is_empty()):
			data = self.s_reverse.peek()
			print("%d | " % (data), end='')
			self.s.push(data)
			self.s_reverse.pop()

		print()

if __name__ == '__main__':

	q = MyQueue()

	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)

	q.print()

	q.dequeue()

	q.print()

	q.enqueue(5)
	q.enqueue(6)

	q.print()


