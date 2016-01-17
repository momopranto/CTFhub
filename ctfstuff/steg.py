from PIL import Image
import binascii
png = Image.open('steg1.png')
pix = png.load()
png.size
for i in xrange (0,300):
	print '%02x%02x%02x' % (pix[i,0][0],pix[i,0][1],pix[i,0][2]),
for i in xrange (0,300):
    print '%02x%02x%02x' % (pix[i,1][0],pix[i,1][1],pix[i,1][2]),
string = ''
for i in xrange (0,800):
    r,g,b = pix[i,0]
    r -= 254
    g -= 254
    b -= 254
    string += str(r) + str(g) + str(b)
print binascii.unhexlify('%x' % int(string,2))