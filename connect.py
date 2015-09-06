import ibmiotf.device
import time
import grovepi

try:
	options = ibmiotf.device.ParseConfigFile("/Desktop/IoT/device.cfg")
	client = ibmiotf.device.Client(options)
	client.connect()

	ultrasonic_ranger = 4
	while True:
		try:
		    # Read distance value from Ultrasonic
		    reading = grovepi.ultrasonicRead(ultrasonic_ranger)
		except:
		    print ("Error reading ultrasonic")
		myData={'distance' : reading}
		client.publishEvent("status", "json", myData)
		time.sleep(10)

except ibmiotf.ConnectionException  as e:
	print(e)