import ibmiotf.device

try:
  options = {
    "org": "z4cnep",
    "type": "RaspberryPi",
    "id": "000000001bb887a7",
    "auth-method": "token",
    "auth-token": "6xzR?XvuXGVd2+k?qq"
  }
  client = ibmiotf.device.Client(options)
except ibmiotf.ConnectionException  as e:
	print("error")

client.connect()
myData={'name' : 'foo', 'cpu' : 60, 'mem' : 50}
client.publishEvent(event="status", msgFormat="json", data=myData)