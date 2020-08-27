"""
PROBLEM

Three in One: 
* Describe how you could use a single array to implement three stacks. 
"""




class Stack:
	def __init__(self, n):
		self.stack_n = n
		self.start = 0
		self.top = 0

		def is_empty(self):
			return self.top == self.start



class ThreeInOne:
	def __init__(self):
		self.list = []
		self.s1 = Stack(1)
		self.s2 = Stack(2)
		self.s3 = Stack(3)

	def push(self, n, item):
		if n == 1:
			self.list = [item] + self.list
			self.s1.start += 1
			self.s2.start += 1
			self.s2.top += 1
			self.s3.start += 1
			self.s3.top += 1

		elif n == 2:
			self.list = self.list[:self.s2.top] + [item] + self.list[self.s2.top:]
			self.s2.top += 1
			self.s3.start += 1
			self.s3.top += 1
		else:
			self.list += [item]
			self.s3.top += 1

	def pop(self, n):
		if n == 1:
			self.list = self.list[1:]
			self.s1.start -= 1
			self.s2.start -= 1
			self.s2.top -= 1
			self.s3.start -= 1
			self.s3.top -= 1

		elif n == 2:
			self.list = self.list[:self.s2.top-1] + self.list[self.s2.top:]
			self.s2.top -= 1
			self.s3.start -= 1
			self.s3.top -= 1
		else:
			self.list = self.list[:-1]
			self.s3.top -= 1




if __name__ == '__main__':

	t = ThreeInOne()

	t.push(1, 4)
	t.push(1, 3)
	t.push(1, 2)
	t.push(1, 1)

	print(t.list)

	t.push(2, 5)
	t.push(2, 6)
	t.push(2, 5)
	t.push(2, 7)

	print(t.list)

	t.pop(2)
	t.pop(2)

	print(t.list)

	t.push(2, 7)
	t.push(2, 8)

	print(t.list)

	t.push(3, 9)
	t.push(3, 10)

	print(t.list)

	t.push(2, 7)
	t.push(2, 7)
	t.push(2, 7)
	t.push(2, 7)

	print(t.list)

