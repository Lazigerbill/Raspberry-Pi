import time
import ibmiotf.device
from grovepi import grovepi

try:
	options = ibmiotf.device.ParseConfigFile('/home/pi/Desktop/IoT/device.cfg')
	client = ibmiotf.device.Client(options)
	client.connect()

	while True:
		# define pin number for sensors here
		dht = 4
		light_sensor = 1
		sound_sensor = 0
		try:
			temp = grovepi.dht(dht,0)[0]
		except: 
			temp = 'Sensor error!'
		try:
			humidity = grovepi.dht(dht,0)[1]
		except:
			humidity = 'Sensor error!'
		try:
			lightlvl = grovepi.analogRead(light_sensor)
		except:
			lightlvl = 'Sensor error!'
		try:
			soundlvl = grovepi.analogRead(sound_sensor)
		except:
			soundlvl = 'Sensor error!'

		myData={'temp':temp, 'humidity':humidity, 'lightlvl':lightlvl, 'soundlvl':soundlvl}
		client.publishEvent("IC306A", "json", myData)
		time.sleep(60)

except ibmiotf.ConnectionException as e:
	print(e)



