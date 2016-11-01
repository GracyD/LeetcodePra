class Solution:
	def generateTriangle(self, numRows):
		
		if numRows == 0:
			return result
		if numRows == 1:
			result = [[1]]
			return result

		result = [[] for i in range(numRows)]
		result[0] = [1]
		result[1] = [1,1]

		for each_row in range(2, numRows):
			result[each_row] = [1 for j in range(each_row+1)]
			for item in range(1, each_row):
				result[each_row][item] = result[each_row-1][item-1] + result[each_row-1][item]
		return result[numRows-1]


if __name__ == '__main__':
	sol = Solution()
	triangle = sol.generateTriangle(5)
	print triangle