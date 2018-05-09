#
#  http.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2017 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from .http import Http
import json

class Auth:

	def login(username,password):
		Http.postRequest("https://auth.roblox.com/v2/login",{})

	def logout():
		Http.sendRequest("https://auth.roblox.com/v2/logout")