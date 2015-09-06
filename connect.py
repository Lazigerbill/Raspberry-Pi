import ibmiotf.device
import time
import grovepi

try:
	options = {
    "org": "z4cnep",
    "type": "RaspberryPi",
    "id": "000000001bb887a7",
    "auth-method": "token",
    "auth-token": "6xzR?XvuXGVd2+k?qq"
  }
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