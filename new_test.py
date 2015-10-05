import time
from datetime import datetime
from grovepi import grovepi

while True:
	# define pin number for sensors here
	dht = 4
	light_sensor = 1
	sound_sensor = 0
	moist_sensor = 2
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
		soundlvl = grovepi.analogRead(sound_sensor)
	except:
		soundlvl = None
	try:
		moistlvl = grovepi.analogRead(moist_sensor)
	except:
		moistlvl = None


	# timestamp is UTC, and UTC time shall be used across
	myData={"d": {'temp':temp, 'humidity':humidity, 'lightlvl':lightlvl, 'soundlvl':soundlvl, 'moistlvl':moistlvl}, "ts": datetime.utcnow().isoformat()+"Z"}
	print(myData)
	time.sleep(6)


# def myCommandCallback(cmd):
#   print("Command received: %s" % cmd.data)
#   if cmd.command == "TurnOn":
#     grovepi.digitalWrite(2,1)
#     print("LED is now turned ON")
#   elif cmd.command == "TurnOff":
#     grovepi.digitalWrite(2,0)
#     print("LED is now turned ON")


