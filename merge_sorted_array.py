class Solution:
	def merge_array(self, A, B):
		i = len(A) - 1
		j = len(B) - 1
		x = len(A) + len(B) -1

		while x >= 0:
			if i >= 0 and j >= 0:
				if A[i] > B[j]:
					A[x] = A[i]
					i -= 1
				else:
					A[X] = B[j]
					j -= 1
			elif i >= 0:
				A[x] = A[i]
				i -= 1
			elif j >= 0:
				A[x] = A[j]
				i -= 1
			x -= 1

