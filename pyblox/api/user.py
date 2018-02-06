#
#  user.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2018 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from __future__ import absolute_import
from .http import Http
import json

class User(object):
	
	#GET https://www.roblox.com/UserCheck/DoesUsernameExist?username={username}
	#Returns Boolean
	def checkUsernameExists(username):
		a = Http.sendRequest(u"https://www.roblox.com/UserCheck/DoesUsernameExist?username="+unicode(username))
		b = a.decode(u"utf-8")
		c = json.loads(b)
		if c[u"success"] == u"True" or True:
			return True
		else:
			return False

	#GET https://api.roblox.com/users/get-by-username?username={username}
	#Returns Table/Array + Attributes
	def getUser(username):
		a = Http.sendRequest(u"https://api.roblox.com/users/get-by-username?username="+unicode(username))
		b = a.decode(u"utf-8")
		c = json.loads(b)
		global User
		User = lambda: None
		User.Id = c[u"Id"]
		User.Username = c[u"Username"]
		User.AvatarUrl = c[u"AvatarUri"]
		User.AvatarFinal = c[u"AvatarFinal"]
		User.IsOnline = c[u"IsOnline"]
		return User

	#GET https://www.roblox.com/Asset/BodyColors.ashx?userId={userId}
	#Returns Table/Array
	def getUserBodyColors(id):
		a = Http.sendRequest(u"https://www.roblox.com/Asset/BodyColors.ashx?userId="+unicode(id))
		return a

	#GET https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId={userId}
	#Returns Table/Array
	def getAssetsWorn(id):
		a = Http.sendRequest(u"https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId="+unicode(id))
		return a

	#GET https://www.roblox.com/Asset/CharacterFetch.ashx?userId={userId}&placeId={placeId}
	#Returns Table/Array
	def getAssetVersions(id,placeid):
		a = Http.sendRequest(u"https://www.roblox.com/Asset/CharacterFetch.ashx?userId="+unicode(id)+u"&placeId="+unicode(placeid))
		return a

	#GET https://www.roblox.com/Contests/Handlers/Showcases.ashx?userId={userId}
	#Returns Table/Array
	def getUserPlaces(id):
		a = Http.sendRequest(u"https://www.roblox.com/Contests/Handlers/Showcases.ashx?userId="+unicode(id))
		return a

	#GET https://www.roblox.com/badges/roblox?userId={userId}&imgWidth=110&imgHeight=110&imgFormat=png
	#Return Table/Array
	def getUserBadges(id):
		a = Http.sendRequest(u"https://www.roblox.com/badges/roblox?userId="+unicode(id)+u"&imgWidth=110&imgHeight=110&imgFormat=png")
		return a
