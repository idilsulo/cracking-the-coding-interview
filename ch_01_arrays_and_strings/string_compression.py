"""
PROBLEM

Notes:
* Implement a method to perform basic string compression using the counts of repeated characters. 
* For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, 
	your method should return the original string. 
* You can assume the string has only uppercase and lowercase letters (a - z).

"""

"""
* Time Complexity: O(N), N:length of string
* Space Complexity: O(N), allocating another string, grows with the size of input

"""
def string_compression(s : str) -> str:

	compressed = ""
	if len(s) == 0:
		return compressed

	prev = s[0]
	val = 1
	flag = False
	
	for c in s[1:]:

		if prev == c:
			val += 1
		else:
			compressed += prev
			compressed += str(val)
			val = 1
			prev = c

	compressed += prev
	compressed += str(val)
	
	if len(compressed) < len(s):
		return compressed
	else:
		return s


if __name__ == '__main__':
	print("TEST CASE #1 : %r" % (string_compression('aabcccccaaa')))
	print("TEST CASE #2 : %r" % (string_compression('abcde')))
	print("TEST CASE #3 : %r" % (string_compression('abcdde')))
	print("TEST CASE #4 : %r" % (string_compression('abcccc')))
	print("TEST CASE #4 : %r" % (string_compression('abccccddeeeee')))
	print("TEST CASE #5 : %r" % (string_compression('')))
	print("TEST CASE #6 : %r" % (string_compression('A')))




