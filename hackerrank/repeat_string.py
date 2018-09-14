def repeatedString(s, n):
	l = len(s)
	rem = n % l
	div = n / l
	rem_a = 0
	count_a = 0
	for i in range(l):
		if(s[i] == 'a'):
			count_a = count_a +1
			if i < rem:
				rem_a = rem_a + 1

	return div*count_a + rem_a

print repeatedString("ceebbcb", 817723)
print repeatedString("ebcdddafdfeffaddbceddebafbbebebbbcefcbcdfbaabecfaaeeaaffdfccffbdeeaabcfeecfcecbfebacefebdfaeedadebdf", 561984209086)