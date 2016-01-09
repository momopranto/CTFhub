txt = "rhtabeoatksoatkeoa"
key1 = [0x14, 0x4, 0x15, 0x6]
key = [0x65, 0x6f, 0x61, 0x74, 0x6b]
 

def my_xor(cipher, key):
	keylen = 5
	res = ""
	for i in range(len(cipher)):
		if ((i+1)%5 == 0):
			res += chr(ord(cipher[i]) ^ 0x0)
		else:
			res += chr(ord(cipher[i]) ^ key[i%4])
	return res

print my_xor(txt,key)