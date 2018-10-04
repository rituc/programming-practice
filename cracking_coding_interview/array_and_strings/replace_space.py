def replace_space(str1):
	space_count = 0
	n = len(str1)
	for i in range(len(str1)):
		if(str1[i] == " "):
			space_count = 1 + space_count
	new_len = len(str1) + 2 * space_count
	str1 = str1 + [0] * 2 * space_count

	for i in range(n-1, 0, -1):
		if(str1[i] == " "):
			str1[new_len - 1] = '%'
			str1[new_len - 2] = '2'
			str1[new_len - 3] = '0'
			new_len = new_len - 3
		else:
			str1[new_len - 1] = str1[i]
			new_len = new_len -1
	return ''.join(str1)

print replace_space(list("I am good"))

