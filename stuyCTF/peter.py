txt = "1225951bcf0ec5889dab77c8e48749582b9f3906e979038fe4ae4508c13c5cd536a45a1462f5f3525668af7f46b370bb631a70b90399f3b7fa80de225361e5cbf03796ce6b8c171abc2f47dbe08db6016d8871"
key1 = [0x14, 0x4, 0x15, 0x6]
key = [0x6e, 0x74, 0x66, 0x73]
 

def my_xor(cipher, key):
	keylen = 4
	res = ""
	for i in range(len(cipher)):
		res += chr(ord(cipher[i]) ^ key[i%4])
	return res

print my_xor(txt,key)