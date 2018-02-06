#
#  http.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2018 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from __future__ import absolute_import
import json
import requests

class Http(object):

	# GET Request
	# Params: "url" // target url
	def sendRequest(url):
		payload = requests.get(unicode(url))
		statusCode = payload.status_code
		header = payload.headers
		content = payload.content
		if statusCode is not 200:
			return print u"[Pyblox][GET] Something went wrong. Error: "+statusCode
		return content

	# POST Request
	# Params: "url" // target url, payload // {JSON key-value pairs}
	def postRequest(url,payload):
		payload = requests.post(unicode(url), data = payload)
		statusCode = payload.status_code
		header = payload.headers
		content = payload.content
		if statusCode is not 200:
			return print u"[Pyblox][POST] Something went wrong. Error: "+statusCode
		return content
