from socket import *

inputs = []
for x in range(1,1000):
	inputs.append(str(x))

n = 0
while True:
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(("python.sctf.io",11236))
	s.recv(420)
	s.send(inputs[n%len(inputs)])
	resp = s.recv(420)
	if resp != "Nope!":
		print "------\n" + resp
		break
	else:
		print inputs[n%len(inputs)] + " => " + resp
		n += 1
		

s.close()
