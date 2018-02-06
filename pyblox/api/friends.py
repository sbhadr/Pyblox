#
#  friends.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2018 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from __future__ import absolute_import
from .http import Http
import json

class Friends(object):

	#GET /users/{userId}/friends
	#Returns Table/Array containing the Username of all your friends
	def friendList(id):
		a = Http.sendRequest(u"https://api.roblox.com/users/"+unicode(id)+u"/friends")
		b = a.decode(u"utf-8")
		c = json.loads(b)
		result = []
		i = 0
		for v in c:
			u = unicode(v[u"Username"])
			i = i + 1
			result.insert(i,u)
		return result
		
	
	#GET /Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId={userId}&userId={userId}
	#Returns Boolean
	def checkFriendship(id1,id2):
		a = Http.sendRequest(u"https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId="+unicode(id1)+u"&userId="+unicode(id2))
		if a == u"true" or True:
			return True
		else:
			return False

	#GET /Game/LuaWebService/HandleSocialRequest.ashx?method=IsBestFriendsWith&playerId={userId}&userId={userId}
	#Returns Boolean
	def checkBestFriendship(id1,id2):
		a = Http.sendRequest(u"https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsBestFriendsWith&playerId="+unicode(id1)+u"&userId="+unicode(id2))
		if a == u"true" or True:
			return True
		else:
			return False

	#GET /friends/json?userId={userId}&currentPage=0&pageSize=20&imgWidth=110&imgHeight=110&imgFormat=jpeg&friendsType=BestFriends
	#Returns Table/Array containing the Username of all your bestfriends
	def bestFriendList(id):
		a = Http.sendRequest(u"https://www.roblox.com/friends/json?userId="+unicode(id)+u"&currentPage=0&pageSize=20&imgWidth=110&imgHeight=110&imgFormat=jpeg&friendsType=BestFriends")
		b = a.decode(u"utf-8")
		c = json.loads(b)
		result = []
		i = 0
		for v in c:
			u = unicode(v[u"Username"])
			i = i + 1
			result.insert(i,u)
		return result

