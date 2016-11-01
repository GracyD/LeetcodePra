class Solution:
	def generateTriangle(self, numRows):
		
		if numRows == 0:
			return result
		if numRows == 1:
			result = [[1]]
			return result
		if numRows == 2:
			result = [[1], [1,1]]
			return result
		if numRows > 2:
			result = [[] for i in range(numRows)]
			for each_row in range(numRows):
				result[each_row] = [1 for j in range(each_row + 1)]
			for each_row in range(2, numRows):
				for item in range(1, each_row):
					result[each_row][item] = result[each_row-1][item-1] + result[each_row-1][item]
			return result



if __name__ == '__main__':
	sol = Solution()
	triangle = sol.generateTriangle(5)
	for row in triangle:
		print row

        