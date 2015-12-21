import qrtools

for n in range(1,61):
	qr = qrtools.QR()
	if n < 10:
		qr.decode("frame-00"+str(n)+".png")
	else:
		qr.decode("frame-0"+str(n)+".png")
	print qr.data
