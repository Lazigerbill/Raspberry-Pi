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
	client.connect()
	myQosLevel = 1
	logging.info("IBM IoTF connected successfully, QoS Level at %i" % myQosLevel)
except Exception, e:
	logging.debug(str(e))
	print str(e)

#Loop starts here:
while True:
	myData={'txt': 'hello world', 'ts': datetime.datetime.utcnow().isoformat()+'Z'}
	client.publishEvent("IC306A", "json", myData, myQosLevel)
	time.sleep(5)