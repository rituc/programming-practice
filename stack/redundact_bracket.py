# https://www.interviewbit.com/problems/redundant-braces/

def check_redundancy(str):
	stack = []
	for i in str:
		if i == ')':
			top = stack[-1]
			stack.pop()
			flag = 1

			while(top != '('):
				if(top == '+' or top == '-' or top == '*' or top == '/'):
					flag =0
				top = stack[-1]
				stack.pop()

			if flag == 1:
				return 1
		else:
			stack.append(i)
	return 0



print check_redundancy("((a+b))")
print check_redundancy("a+(b)")
print check_redundancy("(a+b)")
print check_redundancy("(a+(a+b))")