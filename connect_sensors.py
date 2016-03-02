import time
from datetime import datetime
import ibmiotf.device #install by 'sudo pip install ibmiotf' on the Rpi
import grovepi #run setup.py in the grovepi directory

try:
	options = ibmiotf.device.ParseConfigFile('/etc/sensors.cfg')
	client = ibmiotf.device.Client(options)
	client.connect()
	
	while True:
		# define pin number for sensors here
		dht = 7
		light_sensor = 2
		moist_sensor = 0
		try:
			temp = grovepi.dht(dht,0)[0]
		except: 
			temp = None
		try:
			humidity = grovepi.dht(dht,0)[1]
		except:
			humidity = None
		try:
			lightlvl = grovepi.analogRead(light_sensor)
		except:
			lightlvl = None
		try:
			moistlvl = grovepi.analogRead(moist_sensor)
		except:
			moistlvl = None

		myQosLevel=1

		# timestamp is UTC, and UTC time shall be used across
		myData={'d': {'temp':temp, 'humidity':humidity, 'lightlvl':lightlvl, 'moistlvl':moistlvl}, 'ts': datetime.utcnow().isoformat()+'Z'}
		client.publishEvent("IC306A", "json", myData, myQosLevel)
		time.sleep(30)

except ibmiotf.ConnectionException as e:
	print(e)

# def myCommandCallback(cmd):
#   print("Command received: %s" % cmd.data)
#   if cmd.command == "TurnOn":
#     grovepi.digitalWrite(2,1)
#     print("LED is now turned ON")
#   elif cmd.command == "TurnOff":
#     grovepi.digitalWrite(2,0)
#     print("LED is now turned ON")

