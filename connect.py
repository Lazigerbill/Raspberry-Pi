import time
import grovepi
import serial, httplib



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
		  myData={'distance' : grovepi.ultrasonicRead(ultrasonic_ranger)}
		  client.publishEvent("status", "json", myData)
		  time.sleep(10)
		except:
			print ("Error reading ultrasonic")
			

except ibmiotf.ConnectionException  as e:
	print(e)


def sendRequest(reading):
	headers = {"Contect-type": "application/x-www-form-urlencoded"}
	conn = httplib.HTTPConnection("knuckleballers.mybluemix.net")
	conn.request("POST", "/server_post", "reading=" +readings, headers)
	repsonse = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()