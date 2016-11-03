def jumping(jumping_list):
	if len(jumping_list) == 0:
		return True
	v = jumping_list[0]

	for i in range(len(jumping_list)):
		v -= 1
		if v < 0:
			return False

		if v < jumping_list[i]:
			v = jumping_list[i]

	return True

s1 = [2,3,1,1,4]
s2 = [3,2,1,0,4]
print jumping(s1)
print jumping(s2)