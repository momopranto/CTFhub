import hashlib

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for n in range(99):
	for a in alpha:
		for i in range(999):
			x = str(n) + a + str(i)
			if (hashlib.md5(x).hexdigest() == "0ab1a9222a15da1159eb94212c5c8baf"):
				print x
			
