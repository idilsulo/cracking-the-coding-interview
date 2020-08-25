"""
PROBLEM

String Rotation:
* Assume you have a method isSubstring which checks if one word is a substring of another. 
* Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using 
	only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
"""

def is_rotation(s1 : str, s2 : str) -> bool:

	if len(s1) != len(s2):
		return False

	xor = 0
	for c1,c2 in zip(s1,s2):
		xor ^= ord(c1)
		xor ^= ord(c2)

	return xor == 0

if __name__ == '__main__':
	print("TEST CASE #1 : %r" % (is_rotation('abcd', 'cbda')))
	print("TEST CASE #2 : %r" % (is_rotation('abdcd', 'cbdaa')))

