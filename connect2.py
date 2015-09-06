import time
import grovepi
import httplib



ultrasonic_ranger = 4
while True:
	try:
	  # Read distance value from Ultrasonic
	  sendRequest(str(grovepi.ultrasonicRead(ultrasonic_ranger)))
	except:
		print ("Error reading ultrasonic")
		time.sleep(10)
			




def sendRequest(reading):
	headers = {"Contect-type": "application/x-www-form-urlencoded"}
	conn = httplib.HTTPConnection("knuckleballers.mybluemix.net")
	conn.request("POST", "/server_post", "reading=" +readings, headers)
	repsonse = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()