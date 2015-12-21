import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_odd(n):
	if n % 2 == 1:
		return True;
	
flufferduffers = 0
for x in range(1000):
	odd_sum = 0
	for i in range(x):
		if is_odd(i):
			odd_sum += i
	prime_sum = 0
	if x > 2:	
		for i in range(2,x):
			if is_prime(i):
				prime_sum += i
	if prime_sum - odd_sum < 0:
		flufferduffers += 1

print flufferduffers