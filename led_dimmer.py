import time
import datetime
import ibmiotf.device
import logging
# logging.basicConfig(filename='/home/pi/Raspberry-Pi/rs485.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(filename='/home/pi/Documents/logs/led_dimmer.log', level=logging.DEBUG)

#connect to IBM IoTF
try:
	options = ibmiotf.device.ParseConfigFile('/etc/rpi_iotf/ledpod.cfg')
	client = ibmiotf.device.Client(options)
	# myQosLevel = 1
	client.connect()
	# logging.info("IBM IoTF connected successfully, QoS Level at %i" % myQosLevel)
	client.commandCallback = myCommandCallback
except ibmiotf.ConnectionException as e:
	logging.debug(str(e))
	print str(e)

#Loop starts here:
while True:
	myData={'txt': 'hello world', 'ts': datetime.datetime.utcnow().isoformat()+'Z'}
	client.publishEvent("IC306A", "json", myData, myQosLevel)
	time.sleep(5)




def myCommandCallback(cmd):
	print("Command received: %s" % cmd.data)
	# if cmd.command == "setInterval":
	# 	if 'interval' not in cmd.data:
	# 		print("Error - command is missing required information: 'interval'")
	# 	else:
	# 		interval = cmd.data['interval']
	# 	elif cmd.command == "print":
	# 		if 'message' not in cmd.data:
	# 			print("Error - command is missing required information: 'message'")
	# 		else:
	# 			print(cmd.data['message'])