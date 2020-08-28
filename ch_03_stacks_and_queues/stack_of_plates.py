"""
PROBLEM

Stack of Plates: 
* Imagine a (literal) stack of plates. If  the stack gets too high, it might topple. 
* Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
* Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and 
	should create a new stack once the previous one exceeds capacity. 
* SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack 
	(that is, pop () should return the same values as it would if there were just a single stack). 

FOLLOW UP 
* Implement a function popAt (int  index) which performs a pop operation on a specific sub-stack.
"""

class StackNode:
	def __init__(self, x):
		self.data = x
		self.next = None

class SetOfStacks:
	def __init__(self, node_limit=5):
		self.stacks = []
		self.node_count = 0
		self.node_limit = node_limit
		self.top = None

	def is_empty(self):
		return len(self.stacks) == 0

	def push(self, item):
		node = StackNode(item)

		if self.node_count < self.node_limit:
			if self.node_count == 0:
				self.stacks.append(node)
			else:
				node.next = self.top
			self.node_count += 1
		else:
			self.stacks.append(node)
			self.node_count = 1
		
		self.top = node
		self.stacks[-1] = node
		

	def pop(self):
		if self.node_count == 0:
			print("Stack is empty, pop() cannot be performed.", end='\n\n')
		elif self.node_count == 1:
			self.stacks = self.stacks[:-1]
			if(len(self.stacks) > 0):
				self.node_count = 5
				self.top = self.stacks[-1]
			else:
				self.node_count = 0
		else:
			self.top = self.top.next
			self.stacks[-1] = self.top
			self.node_count -= 1


	# TO-DO: Define pop at
	def pop_at(self):
		pass

def pretty_print(stacks):

	print("****START-SET-OF-STACKS****")
	
	for s in stacks:
		print("---START-STACK---")
		while s:
			print("   -----")
			print("   |   |")
			print("   | " + str(s.data) + " |")
			print("   |   |")
			print("   -----")
			s = s.next
		print("---END-STACK---")
	
	print("*****END-SET-OF-STACKS*****", end='\n\n')


if __name__ == '__main__':

	s = SetOfStacks()

	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)

	pretty_print(s.stacks)

	s.pop()
	s.pop()

	pretty_print(s.stacks)


	s.push(3)
	s.push(4)
	s.push(5)
	s.push(4)
	s.push(4)
	s.push(5)
	s.push(6)
	s.push(7)

	pretty_print(s.stacks)

	s.pop()
	s.pop()
	s.pop()
	s.pop()
	s.pop()
	s.pop()

	pretty_print(s.stacks)

	s.pop()
	s.pop()
	s.pop()
	s.pop()

	pretty_print(s.stacks)

	s.pop()

	pretty_print(s.stacks)
