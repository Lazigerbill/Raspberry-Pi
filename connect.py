import ibmiotf.device
import time

try:
  options = {
    "org": "z4cnep",
    "type": "RaspberryPi",
    "id": "000000001bb887a7",
    "auth-method": "token",
    "auth-token": "6xzR?XvuXGVd2+k?qq"
  }
  client = ibmiotf.device.Client(options)
	client.connect()

	while True:
		myData={'name' : 'foo', 'cpu' : 60, 'mem' : 50}
		client.publishEvent(event="status", msgFormat="json", data=myData)
		time.sleep(1)

except ibmiotf.ConnectionException  as e:
	print("error")