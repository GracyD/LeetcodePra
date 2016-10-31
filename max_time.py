#Given random 4 digits. Print the maximum time it can make up. If not, warning should be given.

class Solution:
	def max_time(self, numls):
		result = []
		tmp = numls
		if self.max_num(2, tmp) == 2:
			first_hour = self.max_num(2, tmp)
			result.append(first_hour)
			tmp.remove(first_hour)
			sec_ran = 3
		elif self.max_num(2, tmp) == 0 or self.max_num(2, tmp) == 1:
			first_hour = self.max_num(2, tmp)
			result.append(first_hour)
			tmp.remove(first_hour)
			sec_ran = 9
		
		if result != []:
			if self.max_num(sec_ran, tmp) != None:
				second_hour = self.max_num(sec_ran, tmp)
				result.append(second_hour)
				tmp.remove(second_hour)
				if self.max_num(5, tmp) != None:
					first_minute = self.max_num(5, tmp)
					result.append(first_minute)
					tmp.remove(first_minute)
					if self.max_num(9, tmp) != None:
						second_minute = self.max_num(9, tmp)
						result.append(second_minute)
						print "Maximum Time is: %d%d:%d%d" % (result[0], result[1], result[2], result[3])
				else:
					print "No first minute digit found. Not valid time."
			else:
				print "No second hour digit found. Not valid time."
		else:
			print "No first hour digit found. Not valid time."

	def max_num(self, ran, s):
		max = None
		for i in s:
			if i <= ran and i > max:
				max = i
		return max


if __name__ == '__main__':
	sol = Solution()
	s1 = [1,2,3,4]
	s2 = [2,9,9,9]
	s3 = [2,2,3,3]
	s4 = [0,5,4,5]
	s5 = [9,0,1,0]
	s6 = [3,6,3,7]

	sol.max_time(s1)
	sol.max_time(s2)
	sol.max_time(s3)
	sol.max_time(s4)
	sol.max_time(s5)
	sol.max_time(s6)
