from flowthings import API, Token, mem
from subprocess import PIPE, Popen
from time import sleep
import psutil

ACCOUNT_NAME = "qxzhiwrtnr"
FLOW_PATH = "/qxzhiwrtnr"
ACCOUNT_TOKEN = "5hJHAdCNhYP1jvdUGmLeKD3UDBT9"

#get cpu temperature

def cpu_temp():
	process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
	output, error = process.communicate()
	return float(output[output.index('=') + 1:output.index("'")])

def drop():
	drop = {
		"elems": {
			"cpu_temp": {
			"type": "float",
			"value": cpu_temp()
			},
			"ram": {
			"type": "map",
			"value": {}
			},
			"disk": {
			"type": "map",
			"value": {}
			}
		}	
	}

	ram = psutil.virtual_memory()
	drop['elems']['ram']['value']['total'] = ram.total / 2 ** 20
	drop['elems']['ram']['value']['used'] = ram.used / 2 ** 20
	drop['elems']['ram']['value']['free'] = ram.free / 2 ** 20

	disk = psutil.disk_usage('/')
	drop['elems']['disk']['value']['total'] = disk.total / 2 ** 20
	drop['elems']['disk']['value']['used'] = disk.used / 2 ** 20
	drop['elems']['disk']['value']['free'] = disk.free / 2 ** 20

	return drop

 # setup your credentials
creds = Token(ACCOUNT_NAME, ACCOUNT_TOKEN)

# have the api use the credentials
api = API(creds)

# find flow id 
flows = api.flow.find(mem.path == FLOW_PATH)
flow_id = flows[0]['id']

# loop to create drops in flow
while True:
	new_drop = api.drop(flow_id).create(drop())
	sleep(60)