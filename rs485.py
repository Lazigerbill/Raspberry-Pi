import time
# import ibmiotf.device
import minmalmodbus

#Define port and slave address(decimal) here
instr = minimalmodbus.Instrument("/dev/ttyAMA0", 1) 

while True:
	try: 
		fq = instr.read_float(int('4000',16)) 
		v1 = instr.read_float(int('4002',16))
		v12 = instr.read_float(int('400a',16))
		current = instr.read_float(int('4012',16))
		apower = instr.read_float(int('401c',16))
	except Exception, e:
		print str(e)

	print "Frequency: " + fq
	print "Phase Voltage: " + v1
	print "Line Voltage: " + v12
	print "Current: " + current
	print "Phase A Power: " + apower

	time.sleep(3000)