import time
import datetime
import ibmiotf.device
import wiringpi2 as wiringpi  
import logging
# logging.basicConfig(filename='/home/pi/Raspberry-Pi/rs485.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(filename='/home/pi/Documents/logs/led_dimmer.log', level=logging.DEBUG)

#connect to IBM IoTF
try:
	options = ibmiotf.device.ParseConfigFile('/etc/rpi_iotf/ledpod.cfg')
	client = ibmiotf.device.Client(options)
	myQosLevel = 1
	# logging.info("IBM IoTF connected successfully, QoS Level at %i" % myQosLevel)
except ibmiotf.ConnectionException as e:
	logging.debug(str(e))
	print str(e)

try:
	wiringpi.wiringPiSetupGpio()  
	wiringpi.pinMode(18,2)      # pwm only works on GPIO port 18  
	# wiringpi.pwmWrite(18, 0)  
except Exception, e:
	logging.debug(str(e))
	print str(e)

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)
	print("timestamp: %s" % cmd.timestamp)	
	percent_level = cmd.data["level"]
	pwm_level = int(1024*(percent_level/float(100)));
	print(pwm_level)
	wiringpi.pwmWrite(18, pwm_level)    # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

client.connect()
client.commandCallback = myCommandCallback
#Loop starts here:
while True:
#	myData={'txt': 'hello world', 'ts': datetime.datetime.utcnow().isoformat()+'Z'}
#	client.publishEvent("IC306A", "json", myData, myQosLevel)
	time.sleep(1)



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
