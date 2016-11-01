class Solution:
	def single_num(self, s):
		numls = list(s)
		result = {}
		for i in range(len(numls)):
			if numls[i] in result:
				result[numls[i]] += 1
			else:
				result[numls[i]] = 1
			if result[numls[i]] % 2 == 0:
				del result[numls[i]]
		return result

if __name__ == '__main__':
	sol = Solution()
	s = '1123344422'
	print sol.single_num(s)