from binascii import hexlify, unhexlify
import re
import sys
cipher1 = [2,0xd,0,7,1,0,1,8,1,0xb,0,1,1,1,1,0xf,0,8,1,7,1,7,1,4,0,1,0,7,1,0xc,1,1,0,9,1,0xa,0,0xa]
cipher2 = [3,0xc,0,9,1,3,1,1,1,1,1,0xa,1,0xa,0,0xe,1,8,0,0,0,3,1,2,0,0xd,1,0xa,0,8,1,1,0,9,1,0xa,0,0xa]

flag = [6,6,6,0xc,6,1,6,7]

def strxor(a, b):     # xor two strings of different lengths
 if len(a) > len(b):
   return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
 else:
   return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
 

def xor(s1,s2):
	res = []
	tmp = []
	for i in range(len(s1)):
		res.append(str(hex(s1[i] ^ s2[i])))
	for x in res:
		tmp.append(x[2:])
	s = ''.join(tmp)
	return s
	
czor = strxor(unhexlify("2d0710181b01111f0817171401071c11091a0a"),unhexlify("3c091311111a1a0e180003120d1a0811091a0a"))
print czor
crib = raw_input("Enter crib: ")
for j in range(len(czor)):
	k = czor[j:]
	print "%d "%j + strxor(k,crib)