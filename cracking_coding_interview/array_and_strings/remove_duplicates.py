# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer NOTE: One or two additional variables are fine An extra copy of the array is not

def remove_dups(str1):

	if len(str1) < 2: return str1
	output_str = str1[0]
	str1.sort()

	for i in range(1, len(str1)):
		if(str1[i] != str1[i-1]):
			output_str = output_str + str1[i]

	return output_str

print remove_dups(list("aabbbc"))
print remove_dups(list("aaaa"))
print remove_dups(list("abc"))
print remove_dups("")
print remove_dups(list("ababab"))
