class CountPrime():

	def sieve_of_eratosthenes(self, n):
		prime = [True for i in range(n+1)]
		p = 2
		count = 0
		while(p*p<=n):
			if(prime[p] == True):
				for i in range(p*2, n+1, p):
					prime[i] = False
				p+=1

		for p in range(2,n+1):
			if prime[p]:
				print p,
				count +=1
		return count

def main():

	prime_count = CountPrime().sieve_of_eratosthenes(10)
	print "\nNumber of primes: ", prime_count

if __name__=='__main__':
	main()