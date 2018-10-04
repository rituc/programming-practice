def compress_str(str1):
	count = 1
	s = str1[0]
	for i in range(1, len(str1)):
		if(str1[i] == str1[i-1]):
			count = 1+count
		else:
			s = s + str(count) + str1[i]
			count = 1
	s = s + str(count)
	return s

print compress_str("aaabbbccc")
print compress_str("abc")
print compress_str("a")
print compress_str("aaaaaa")