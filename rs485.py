import time
# import ibmiotf.device
import minimalmodbus

#Define port and slave address(decimal) here
instr = minimalmodbus.Instrument("/dev/ttyAMA0", 1) 
try:
	while True:
		try: 
			fq = instr.read_float(int('4000',16)) 
			v1 = instr.read_float(int('4002',16))
			v12 = instr.read_float(int('400a',16))
			current = instr.read_float(int('4012',16))
			apower = instr.read_float(int('401c',16))
		except Exception, e:
			print str(e)

		print "Frequency: %.2f" % fq
		print "Phase Voltage: %.2f" % v1
		print "Line Voltage: %.2f" % v12
		print "Current: %.2f" % current
		print "Phase A Power: %.2f" % apower

		time.sleep(3000)
		print ("complete...")
except Exception, e:
	print str(e)