def jumping(jumping_list):
	step = 0
	curr = 0
	nex = 0
	i = 0
	length = len(jumping_list)

	while i < length:
		if curr > length - 1:
			break

		while i <= curr:
			nex = max(nex, jumping_list[i] + i)
			i += 1
		step += 1
		curr = nex

	return step

	

s1 = [2,3,1,1,4]

print jumping(s1)
