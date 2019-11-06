def get_primes():
	num = 2
	while True: 
		if is_prime(num):
			yield num
			num +=1 