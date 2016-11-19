import time
import datetime
import ibmiotf.device
import minimalmodbus
import logging
from apscheduler.schedulers.background import BlockingScheduler

#This is the method where data is read from the power meter and then publish MQTT to broker
def readAndPublish():
	try: 
		vAvg = instr.read_float(int('4008',16))
		vLAvg = instr.read_float(int('4010',16))
		iAvg = instr.read_float(int('4018',16))
		pSum = instr.read_float(int('4022',16))
		ts = datetime.datetime.utcnow().isoformat()+'Z'
	except Exception, e:
		logging.debug(str(e))
		print str(e)

	try: 
		myData={'d': {'v1':vAvg, 'v12':vLAvg, 'current':iAvg, 'apower': pSum}, 'ts': ts}
		client.publishEvent("rs485", "json", myData, myQosLevel)	
		print str(myData)


	except Exception, e:
		logging.debug(str(e))
		print str(e)

logging.basicConfig(filename='/home/pi/totem/iot_mqtt.log', filemode='w', level=logging.DEBUG)

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

# setup scheduler here, run every 5 seconds
# stupid scheduler runs on UTC, so beware of DST
sched = BlockingScheduler()
sched.add_job(readAndPublish, 'cron', day_of_week="0-5", hour="0-3,11-23", second="*/5")
sched.start()
