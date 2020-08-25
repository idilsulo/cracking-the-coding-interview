"""
PROBLEM

Check Permutation: 
* Given two strings,write a method to decide if one is a permutation of the
other.
"""


"""
Notes:
* Bit manipulation trick: If all characters in s1 have a corresponding match in s2,
	then they are a permutaion of each other
* Base case should be communicated with the inteviewer clearly: Should having empty strings
	for s1 and s2 return True or False? 0 also has a value in permutation (0! exists), so
	here we consider this case to return True.

* Time Complexity: O(N), N: length of string
* Space Complexity: O(1) -> bit manipulation to the rescue
"""
def check_permutation(s1: str, s2: str) -> bool:
	
	if len(s1) != len(s2):
		return False

	xor = 0
	for i in range(len(s1)):
		xor ^= ord(s1[i])
		xor ^= ord(s2[i])

	if xor == 0:
		return True
	else:
		return False


"""
Notes:
* Alternatively, you can use a hash map as discussed in this chapter

* Time Complexity: O(N), N: length of traversed strings
* Space Complexity: O(1) -> Bit vector has constant size
"""
def check_permutation_alternative(s1: str, s2: str) -> bool:
	
	if len(s1) != len(s2):
		return False

	hash_map = [0] * 128

	for i in range(len(s1)):
		index = ord(s1[i])
		hash_map[index] += 1
	
	for i in range(len(s2)):
		index = ord(s2[i])
		hash_map[index] -= 1

		if hash_map[index] < 0:
			return False

	return True

if __name__ == '__main__':

	print("TEST CASE #1 : %r" % (check_permutation('abcDe', 'ebDca')))
	print("TEST CASE #2 : %r" % (check_permutation('abcDe', 'ebca')))
	print("TEST CASE #3 : %r" % (check_permutation('abcDe', 'ebFca')))
	print("TEST CASE #4 : %r" % (check_permutation('', '')))
	print("TEST CASE #5 : %r" % (check_permutation('a', 'e')))



