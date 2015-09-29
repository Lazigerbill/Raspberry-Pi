import time
import ibmiotf.device

try:
	options = ibmiotf.device.ParseConfigFile('/Users/Bill/Desktop/IoT/Raspberry-Pi/device.cfg')
	client = ibmiotf.device.Client(options)
	client.connect()

except ibmiotf.ConnectionException  as e:
	print(e)
	exit()

while True:
	try:
		myData={'bill' : 'testing', 'chau' : 'testing2'}
	except:
		myData={'bill':'N/A', 'chau':'N/A'}	
	finally:
		client.publishEvent("status", "json", myData)
		time.sleep(300)



