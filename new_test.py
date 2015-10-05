import time
from datetime import datetime
from grovepi import grovepi

while True:
	# define pin number for sensors here
	dht = 4
	light_sensor = 1
	sound_sensor = 0
	moist_sensor = 2

	temp = grovepi.dht(dht,0)[0]
	humidity = grovepi.dht(dht,0)[1]
	lightlvl = grovepi.analogRead(light_sensor)
	soundlvl = grovepi.analogRead(sound_sensor)
	moistlvl = grovepi.analogRead(moist_sensor)


	# timestamp is UTC, and UTC time shall be used across
	myData={"d": {'temp':temp, 'humidity':humidity, 'lightlvl':lightlvl, 'soundlvl':soundlvl, 'moistlvl':moistlvl}, "ts": datetime.utcnow().isoformat()+"Z"}
	print(myData)
	time.sleep(1)


# def myCommandCallback(cmd):
#   print("Command received: %s" % cmd.data)
#   if cmd.command == "TurnOn":
#     grovepi.digitalWrite(2,1)
#     print("LED is now turned ON")
#   elif cmd.command == "TurnOff":
#     grovepi.digitalWrite(2,0)
#     print("LED is now turned ON")


