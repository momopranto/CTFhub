def my_xor(cipher, key):
	keylen = 5
	res = ""
	for i in range(len(cipher)):
		res += chr(ord(cipher[i]) ^ ord(key[i%5]))
	return res

x = None;
with open('note.txt','r') as f:
	x = f.read().lower()

#while len(x) > 25:
#print my_xor(x,'lucas')
print x
print "--------------------\n"


