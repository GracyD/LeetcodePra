class Solution:
	def findMin(self, rotated_list):
		if len(rotated_list) == 0:
			return False
		elif len(rotated_list) == 1:
			return rotated_list[0]
		elif len(rotated_list) == 2:
			return min(rotated_list[0], rotated_list[1])

		start = 0
		end = len(rotated_list) - 1

		while start < end:
			if rotated_list[start] < rotated_list[end]:
				return rotated_list[start]

			mid = start + (end - start) / 2
			if rotated_list[start] < rotated_list[mid]:
				start = mid
			elif rotated_list[start] > rotated_list[mid]:
				end = mid
			else:
				start += 1
		return min(rotated_list[start], rotated_list[end])


if __name__ == '__main__':
	sol = Solution()
	test = [4,5,6,7,0,1,2]
	test2 = [2,3,1,2,2]
	print sol.findMin(test)	
	print sol.findMin(test2)