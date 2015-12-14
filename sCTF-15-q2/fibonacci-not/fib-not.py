glist = [0,1]
wlist = [0,1]

def g(x):
    if (x < len(glist)):
        return glist[x]
    n = (g(x-1) + g(x-2))**2
    glist.append(n)
    return n

def w(x):
    if (x < len(wlist)):
        return wlist[x]
    n = w(x-1)**2 + w(x-2)**2
    wlist.append(n)
    return n

a = g(30)
b = w(30)
c = a-b
print "g(30):" + str(a)
print "w(30):" + str(b)
print "f(30):" + str(c)

s = 0
tmp = c
while (tmp > 0):
    digit = tmp%10
    s = s + digit
    tmp = tmp / 10

print "sum:" + str(s)
