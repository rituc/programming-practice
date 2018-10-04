def generate_nth_fibonacci(n):
	if(n<0): return -1
	if(n==0): return 0
	a = 1
	b = 1
	while(n>2):
		c = a+b
		a = b
		b = c
		n -= 1
	return b

# print generate_nth_fibonacci(0)


def recursive_fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1:
		return recursive_fib(n-1) + recursive_fib(n)
	else:
		return -1

# print generate_nth_fibonacci(10)


def n_fib(n):
	if n<0: return -1
	if n==0: return 0
	a = 0
	b = 1
	for i in range(2, n+1):
		c = a+b
		a=b
		b=c
	return b

print n_fib(-1)
print n_fib(0)
print n_fib(1)
print n_fib(2)
print n_fib(9)
print n_fib(10)

