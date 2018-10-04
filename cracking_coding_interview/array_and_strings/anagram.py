# Write a method to decide if two strings are anagrams or not

def anagram(s1, s2):
	if len(s1) != len(s2):
		return False
	count = [0 for i in range(128)]

	for i in range(len(s1)):
		count[ord(s1[i])] = count[ord(s1[i])] + 1

	for i in range(len(s2)):
		count[ord(s1[i])] -= 1

	for i in range(128):
		if(count[i] !=0):
			return False
	return True


print anagram(list("movie"), list("zzzz"))