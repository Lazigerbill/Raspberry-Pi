import time
import ibmiotf.device
import minimalmodbus

#initiation
try:
	#Define port and slave address(decimal) here
	instr = minimalmodbus.Instrument("/dev/ttyAMA0", 1)

	#connect to IBM IoTF
	options = ibmiotf.device.ParseConfigFile('/etc/rs485.cfg')
	client = ibmiotf.device.Client(options)
	client.connect()
	myQosLevel=1
except Exception, e:
	print str(e)

while True:
	try: 
		fq = instr.read_float(int('4000',16)) 
		v1 = instr.read_float(int('4002',16))
		v12 = instr.read_float(int('400a',16))
		current = instr.read_float(int('4012',16))
		apower = instr.read_float(int('401c',16))
	except Exception, e:
		print str(e)

	myData={'d': {'fq':temp, 'v1':v1, 'v12':v12, 'current':current}, 'apower': apower}
	client.publishEvent("rs485", "json", myData, myQosLevel)	
	print "Frequency: %.2f" % fq
	print "Phase Voltage: %.2f" % v1
	print "Line Voltage: %.2f" % v12
	print "Current: %.2f" % current
	print "Phase A Power: %.2f" % apower
	time.sleep(1)
	print ("complete...")
