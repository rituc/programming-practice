def reverse_str(str):
	start = 0
	end = len(str)-1
	while(start < end):
		temp = str[start]
		str[start] = str[end]
		str[end] = temp
		start +=1
		end -= 1
	return "".join(str)

print reverse_str(list("abc"))