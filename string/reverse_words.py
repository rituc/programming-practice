def reverse_str(str1):
	start, end = 0, len(str1)-1
	while(start<end):
		temp = str1[start]
		str1[start] = str1[end]
		str1[end] = temp
		start +=1
		end -=1

	start_idx = 0
	end_idx = 0

	for i in range(len(str1)):
		if str1[i] == ' ':
			i = i+1
			if(str1[i] == '.' or str1[i] == ' ' or i==len(str1)-1):
				end_idx = i - 1 if i < len(str1) - 1 else i
				while(start_idx<end_idx):
					temp = str1[start_idx]
					if temp != " ":
						str1[start_idx] = str1[end_idx]
						str1[end_idx] = temp
						start_idx += 1
						end_idx -=1
				start_idx =i+1


	return "".join(str1)

print reverse_str(list('i.like.this.program.very.much'))
print reverse_str(list('   the sky is    blue'))
print reverse_str(list('  t   '))
