"""
PROBLEM

Animal Shelter: 
* An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
* People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
	or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
* They cannot select which specific animal they would like. 
* Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, 
	dequeueDog, and dequeueCat. 
* You may use the built-in Linked list data structure. 
"""

import time
class ListNode:
	def __init__(self, x):
		self.type = x
		self.arrival = time.time()
		self.next = None

	def print(self):
		node = self

		print("| %s - Arrived at: %d | " % (node.type, node.arrival))
		node = node.next

		while(node):
			print("-> | %s - Arrived at: %d| " % (node.type, node.arrival))
			node = node.next

		print()



class AnimalShelter():
	def __init__(self):
		self.head = None
		self.last = None

	def enqueue(self, s : str):
		
		node = ListNode(s)

		if not self.head:
			self.head = node
			self.last = self.head
		else:
			self.last.next = node
			self.last = self.last.next

	def dequeue_any(self):
		node = self.head
		self.head = self.head.next
		return node

	def dequeue_dog(self):
		node = self.head
		prev = None
		while(node and node.type != 'dog'):
			prev = node
			node = node.next

		if node:
			if prev: # Previous node exits, update accordingly
				prev.next = node.next
			else: # Previous node does not exist, returned node is the head
				self.head = head.next

			if not node.next: # Node is the last node
				self.last = prev

			return node
		else:
			print("There are currently no dogs in the animal shelter.")
			return None


	def dequeue_cat(self):
		node = self.head
		prev = None
		while(node and node.type != 'cat'):
			prev = node
			node = node.next

		if node:
			if prev: # Previous node exits, update accordingly
				prev.next = node.next
			else: # Previous node does not exist, returned node is the head
				self.head = head.next

			if not node.next: # Node is the last node
				self.last = prev

			return node
		else:
			print("There are currently no cats in the animal shelter.")
			return None


if __name__ == '__main__':

	a = AnimalShelter()
	a.enqueue('cat')
	time.sleep(1)
	a.enqueue('dog')
	time.sleep(1)
	a.enqueue('cat')
	time.sleep(1)
	a.enqueue('cat')
	time.sleep(1)
	a.enqueue('cat')
	time.sleep(1)
	a.enqueue('cat')
	time.sleep(1)
	a.enqueue('dog')
	time.sleep(1)
	a.enqueue('dog')

	a.head.print()

	a.dequeue_dog()

	a.head.print()

	a.dequeue_dog()

	a.head.print()

	a.dequeue_dog()

	a.head.print()

	a.enqueue('cat')

	a.head.print()

	a.dequeue_any()

	a.head.print()

	a.dequeue_dog()



