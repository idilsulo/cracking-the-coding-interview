
"""
PROBLEM

Is Unique: 
* Implement an algorithm to determine if a string has all unique characters. 
* What if you cannot use additional data structures?

"""


"""
Notes:
* In Python, there are two objects that correspond to hash tables: dict and set
* In this case, this function uses dictionary which is an additional data structure 

* Time Complexity: O(N), N: length of string
* Space Complexity: O(N), dictionary storage will be scaled with input string length

""" 
def is_unique_trivial(s: str) -> bool:
	
	look_up = {}
	unique_flag = True

	for c in s:
		if c not in look_up.keys():
			look_up[c] = 1
		else:
			unique_flag = False
			break

	return unique_flag


"""
Notes:
* Use a bit vector instead of dictionary in order to reduce space complexity

* Time Complexity: O(N), N: length of string
* Space Complexity: O(1), bit vector does not scale with input string length

"""
def is_unique(s: str) -> bool:
	
	hash_table = [False] * 128
	unique_flag = True

	for c in s:
		index = ord(c)
		if hash_table[index]:
			unique_flag = False
			break
		else:
			hash_table[index] = 1

	return unique_flag


if __name__ == '__main__':

	print("TEST CASE #1 : %r" % (is_unique("12234AABBBBBC")))
	print("TEST CASE #2 : %r" % (is_unique("1234")))
	print("TEST CASE #3 : %r" % (is_unique("12234")))
	print("TEST CASE #4 : %r" % (is_unique("1")))
	print("TEST CASE #5 : %r" % (is_unique("")))
