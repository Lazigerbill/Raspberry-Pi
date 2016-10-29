import time
import datetime
import ibmiotf.device
import minimalmodbus
import logging
# logging.basicConfig(filename='/home/pi/Raspberry-Pi/rs485.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(filename='/home/pi/totem/iot_mqtt.log', level=logging.DEBUG)

#initialize port
try:
	#Define port and slave address(decimal) here
	instr = minimalmodbus.Instrument("/dev/ttyAMA0", 1)
	logging.info("Port intialized, connected successfully to /dev/ttyAMA0. ")
except Exception, e:
	logging.debug(str(e))

#connect to IBM IoTF
try:
	options = ibmiotf.device.ParseConfigFile('/home/pi/totem/hg_001.cfg') #define path for cfg file
	client = ibmiotf.device.Client(options)
	client.connect()
	myQosLevel = 1
	logging.info("IBM IoTF connected successfully, QoS Level at %i" % myQosLevel)
except Exception, e:
	logging.debug(str(e))
	print str(e)

#Loop starts here:
#single phase power
while True:
	try: 
		fq = instr.read_float(int('4000',16)) 
		v1 = instr.read_float(int('4002',16))
		v12 = instr.read_float(int('400a',16))
		current = instr.read_float(int('4012',16))
		apower = instr.read_float(int('401c',16))
	except Exception, e:
		logging.debug(str(e))
		print str(e)

	try: 
		myData={'d': {'fq':fq, 'v1':v1, 'v12':v12, 'current':current, 'apower': apower}, 'ts': datetime.datetime.utcnow().isoformat()+'Z'}
		client.publishEvent("rs485", "json", myData, myQosLevel)	
		print str(myData)
		# logging.info(str(myData))

		#define read interval here:
		time.sleep(3)

	except Exception, e:
		logging.debug(str(e))
		print str(e)
