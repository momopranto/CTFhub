import hashlib
from itertools import product
from string import ascii_lowercase

#2e561f52df1f1a31b5c4a00d0c846728
alphanum = ascii_lowercase + "1234567890"

#set1 = [''.join(i) for i in product(alphanum,repeat=1)]
#set2 = [''.join(i) for i in product(alphanum,repeat=2)]
#set3 = [''.join(i) for i in product(alphanum,repeat=3)]
#set4 = [''.join(i) for i in product(alphanum,repeat=4)]
#set5 = [''.join(i) for i in product(alphanum,repeat=5)]
set6 = [''.join(i) for i in product(alphanum,repeat=6)]
#set7 = [''.join(i) for i in product(alphanum,repeat=7)]
#set8 = [''.join(i) for i in product(alphanum,repeat=8)]

#combinations = [set1,set2,set3,set4,set5,set6,set7,set8]

for x in set6:
	if (hashlib.md5(x).hexdigest() == "2e561f52df1f1a31b5c4a00d0c846728"):
		print x
