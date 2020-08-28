"""
PROBLEM

Rotate Matrix: 
* Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
	write a method to rotate the image by 90 degrees. 
* Can you do this in place?
"""

"""
Numpy to rule them all! 
But is vectorization really the fastest solution?

Below are the details of the same LeetCode problem with a numpy answer:
* Runtime: 96 ms, faster than 6.51% of Python3 online submissions for Rotate Image.
* Memory Usage: 29 MB, less than 5.09% of Python3 online submissions for Rotate Image.
* Accepted: 437,988 / Submissions: 767,760

Seems like numpy is not that fast after all.
 
"""
import numpy as np

def rotate_matrix_np(m : np.array) -> np.array:
	m = np.array(m)
	return np.rot90(m, 3).tolist()

"""
Maybe add a non-vectorized version later on
"""
def rotate_matrix(m : list) -> list:
	pass


if __name__ == '__main__':
	print("TEST CASE #1 : %r" % (rotate_matrix_np([[1]])))
	print("TEST CASE #2 : %r" % (rotate_matrix_np([[1,2],[3,4]])))
	print("TEST CASE #3 : %r" % (rotate_matrix_np([[1,2,3],[4,5,6],[7,8,9]])))