#
#  http.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

import json
import requests

class Http:

	def sendRequest(url):
		payload = requests.get(str(url))
		statusCode = payload.status_code
		header = payload.headers
		content = payload.content
		if statusCode == 403:
			return print("[Roblox][GET] Something went wrong. Error: 403")
		return content

	def postRequest(url,param1,param2):
		payload = requests.post(str(url), data = {str(param1):str(param2)})
		statusCode = payload.status_code
		header = payload.headers
		content = payload.content
		if statusCode == 403:
			return print("[Roblox][POST] Something went wrong. Error: 403")
		return content