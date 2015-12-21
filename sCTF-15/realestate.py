
estates = None
real1 = []
real2 = []
max = 0.0
max_combo = []
with open('realestate.txt','r') as f:
	estates = f.readlines()
	

for i in range(0,3):
	estates.pop(0)

for l in estates:
	real1.append(l.rsplit(' " '))
	real2.append(l.rsplit(' " '))

for x in real1:
	for y in real2:
		if x[0] != y[0]:
			ratio = (float(x[2])*float(x[3])) + (float(y[2])*float(y[3]))/(float(x[1])+float(y[1]))
			if ratio > max:
				max_combo = [x[0],y[0]]
				max = ratio
				print ratio
			
print max_combo
print max