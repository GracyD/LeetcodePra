class Solution:
	def hammingWeight(self, num):
		count = 0
		n = int(bin(num)[2:])
		while (n > 0):
			count += n & 1;
			n >>= 1;
		return count;

if __name__ == '__main__':
	sol = Solution()
	print sol.hammingWeight(11)
