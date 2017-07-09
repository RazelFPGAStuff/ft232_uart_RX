import serial
ser=serial.Serial(port='COM15',timeout=3)
count = 0
while count < 2000:
	ser.write(b'\xAA')
	count = count + 1
