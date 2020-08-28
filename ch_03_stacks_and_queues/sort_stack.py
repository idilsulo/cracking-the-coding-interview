"""
PROBLEM


Sort Stack: 
* Write a program to sort a stack such that the smallest items are on the top. 
* You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). 
* The stack supports the following operations: push, pop, peek, and isEmpty. 
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

	def print(self):
		s = self.top
		while s:
			print("   -----")
			print("   |   |")
			print("   | " + str(s.data) + " |")
			print("   |   |")
			print("   -----")
			s = s.next

"""
Notes:
* Keep a temporary stack always in sorted order where the largest element is on top.
* Peek at both stacks to decide where the popped element whould go.
"""
def sort(s):
	i = 0
	t = Stack()

	curr_max = s.peek()
	s.pop()

	while(not s.is_empty()):
		s_data = s.peek()
		
		if not t.is_empty():
			t_data = t.peek()

		s.pop()

		i=0
		if (not t.is_empty()) and (s_data < t_data):
			while((not t.is_empty()) and (s_data < t_data)):
				t.pop()
				s.push(t_data)
				if not t.is_empty():
					t_data = t.peek()
				i += 1

			t.push(s_data)

			while(i > 0):
				t.push(s.peek())
				s.pop()
				i -= 1
		else:
			if s_data <= curr_max:
				t.push(s_data)
			else:
				t.push(curr_max)
				curr_max = s_data

	t.push(curr_max)

	while(not t.is_empty()):
		s.push(t.peek())
		t.pop()



if __name__ == '__main__':

	s = Stack()

	s.push(1)
	s.push(5)
	s.push(4)
	s.push(7)
	s.push(3)

	print("Initial stack:")
	s.print()
	print()

	sort(s)

	print("Sorted stack:")
	s.print()
