import requests
import json
import collections 
import config

#constants
WEBHOOK_URL = config.WEBHOOK_URL 
headers = { "Accept" : "application/vnd.tosslab.jandi-v2+json",
	"Content-Type" : "application/json"}

class Connect:
	"""
		JANDI connect object
		element of connectInfo
	"""		
	def __init__(self,title=None,description=None,img_url=None):
		self.title = title
		self.description = description
		self.img_url = img_url
	def to_json(self):
		"""
			convert fron this obj to JSON representation
		"""	
		tmp =  dict(
			title = self.title,
			description = self.description,
			imgUrl = self.img_url
		)	
		this = {}
		#delete empty properties
		for key in tmp:
			if tmp[key]:
				this[key] = tmp[key]	
		return this

def simple_push(message):
	payload = { "body":message } 
	r = requests.post(WEBHOOK_URL,data=json.dumps(payload), headers=headers)
	print(r.text)

def connect_push(message, **kwargs):
	connections = kwargs.get('connections')
	connectionColor = kwargs.get('connectionColor')
	payload = { "body":message,"connectColor" : "#FAC11B", 'connectInfo':[] }

	if not connections:
		raise Exception("connections are not defined")

	#single connection object
	if not isinstance(connections,collections.Iterable):
		payload['connectInfo'].append(connections.to_json())
	#multiple connection objects
	else:
		for con in connections:
			payload['connectInfo'].append(con.to_json())
	r = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
	print(r.text)


if __name__=="__main__":
	simple_push("test")
	con1 = Connect("test","this is test")
	con2 = Connect("test2","this is test")
	connect_push("tst",connections=con1)
	connect_push("tst",connections=[con1,con2])
