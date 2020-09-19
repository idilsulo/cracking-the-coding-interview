"""
PROBLEM

Push Sorted:
* Write a program such that each time push_sorted() is called a new item will be pushed into stack 
	in a way that the sorted order of the nodes of stack will be preserved.
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

def sort(s, item):
	t = Stack()

	while(not s.is_empty()):	
		data = s.peek()
		if(data < item):
			t.push(data)
			s.pop()
		else:
			break

	s.push(item)

	while(not t.is_empty()):
		data = t.peek()
		s.push(data)
		t.pop()

if __name__ == '__main__':


	s = Stack()
	sort(s, 1)
	s.print()
	print()

	sort(s, 5)
	s.print()
	print()

	sort(s, 4)
	s.print()
	print()
	
	sort(s, 7)
	s.print()
	print()

	sort(s, 3)
	s.print()
	print()



