words = None
with open("dictionary.txt","r") as f:
	words = f.readlines()

wordlist = words[0].split(" ")
print len(wordlist)