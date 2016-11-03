class Solution:
	def generateTriangle(self, rowIndex):
		
		if rowIndex == 0:
			return result
		if rowIndex == 1:
			result = [[1]]
			return result

		result = [[] for i in range(rowIndex)]
		result[0] = [1]
		result[1] = [1,1]

		for row in range(rowIndex):
			for item in range(row-1, 0, -1):
				result[item] = result[item] + result [item-1]
		return result

if __name__ == '__main__':
	sol = Solution()
	triangle = sol.generateTriangle(5)
	print triangle



