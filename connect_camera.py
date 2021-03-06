import time
from datetime import datetime
import math
import picamera
import json
import base64
import ibmiotf.device
import random, string

def randomword(length):
  return ''.join(random.choice(string.lowercase) for i in range(length))

def convertImageToBase64():
	with open("live_pic.jpg", "rb") as image_file:
		encoded = base64.b64encode(image_file.read())
	return encoded

def publishEncodedImage(encoded):
	packet_size=3000
	end = packet_size
	start = 0
	length = len(encoded)
	picId = randomword(8)
	pos = 0
	no_of_packets = math.ceil(length/packet_size)

	while start <= len(encoded):
		data = {"d":{"data": encoded[start:end], "pic_id":picId, "pos":pos, "size":no_of_packets}, "ts": datetime.utcnow().isoformat()+"Z"}
		client.publishEvent("Image-Data", "json", data, 0)
		end += packet_size
		start += packet_size
		pos += 1

try:
	options = ibmiotf.device.ParseConfigFile('/etc/camera.cfg')
	client = ibmiotf.device.Client(options)
	client.connect()
	# client.commandCallback = myCommandCallback
	
	while True:
		camera = picamera.PiCamera()
		try:
			camera.vflip = False
			camera.resolution = (480, 560)
			camera.start_preview()
			time.sleep(1)
			camera.capture('live_pic.jpg')
			camera.stop_preview()
			pass
		finally:
			camera.close()

		publishEncodedImage(convertImageToBase64())

		time.sleep(60)

except ibmiotf.ConnectionException as e:
	print(e)



