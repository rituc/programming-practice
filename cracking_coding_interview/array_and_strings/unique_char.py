# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
def unique_char(s):
	count = [ False for i in range(128)]

	for i in range(len(s)):
		if count[ord(s[i])]:
			return False
		else:
			count[ord(s[i])] = True
	return True

print unique_char("moviee")


def unique_char_without_space(s):
	checker = 0
	for i in range(len(s)):
		val = ord(s[i]) - ord('a')
		if checker & (1 << val) > 0:
			return False
		else:
			checker |= 1 << val

