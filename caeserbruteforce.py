plainText = raw_input("What is your plaintext/ciphertext? ")

def caesar(plainText, shift): 
	cipherText = ""
	for ch in plainText:
		if ch.isalpha():
			stayInAlphabet = ord(ch) + shift 
			if stayInAlphabet > ord('z'):
				stayInAlphabet -= 26
			cipherText += chr(stayInAlphabet)
		else:
			cipherText += ch
	print "Shifted " + str(shift) + ": ", cipherText
	return cipherText

for shift in range(26):
	caesar(plainText, shift)
