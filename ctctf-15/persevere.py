x = None;
with open('persevere.txt','r') as f:
	x = f.read()

while len(x) > 25:
	x = x.decode('rot13').decode('base64')
	print x
	print "--------------------\n"


