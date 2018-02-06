#
#  group.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2018 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from __future__ import absolute_import
from .http import Http
from bs4 import *
import html5lib
import urllib2, urllib
import json

class Groups(object):

	#GET /users/{userId}/groups
	#returns table/array with groups + each group's attributes
	def groupList(userid):
		a = Http.sendRequest(u"https://api.roblox.com/users/"+unicode(userid)+u"/groups")
		return a

	#GET /groups/{groupId}
	#Returns Table/Array + Attributes
	def getGroup(groupid):
		a = Http.sendRequest(u"https://api.roblox.com/groups/"+unicode(groupid))
		b = a.decode(u"utf-8")
		c = json.loads(b)
		global Group
		Group = lambda: None
		Group.Name = c[u"Name"]
		Group.Id = c[u"Id"]
		Group.Owner = c[u"Owner"]
		Group.Owner.Name = c[u"Owner"][u"Name"]
		Group.Owner.Id = c[u"Owner"][u"Id"]
		Group.EmblemUrl = c[u"EmblemUrl"]
		Group.Description = c[u"Description"]
		Group.Roles = c[u"Roles"]

	#GET /groups/{groupId}/allies
	#Returns Table/Array with each ally's attributes
	def getGroupAllies(groupid):
		a = Http.sendRequest(u"https://api.roblox.com/groups/"+unicode(groupid)+u"allies")
		return a

	#GET /groups/{groupId}/enemies
	#Returns Table/Array with each enemy's attributes
	def getGroupEnemies(groupid):
		a = Http.sendRequest(u"https://api.roblox.com/groups/"+unicode(groupid)+u"enemies")
		return a
