words = None
ands = []
count = 0
with open("dictionary2.txt","r") as f:
	words = f.readlines()

for x in words:
	if x.find("and") >= 0:
		ands.append(x[:-1])

for y in ands:
	count += len(y)

print ands
print count