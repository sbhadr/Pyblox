#
#  assets.py
#  pyblox
#
#  By Sanjay-B(Sanjay Bhadra)
#  Copyright © 2018 Sanjay-B(Sanjay Bhadra). All rights reserved.
#

from __future__ import absolute_import
from .http import Http
import json


class Assets(object):

	#GET https://www.roblox.com/Game/GetAssetIdsForPackageId?packageId={assetId}
	#Returns Table/Array
	def getPackageAssets(assetid):
		a = Http.sendRequest(u"https://www.roblox.com/Game/GetAssetIdsForPackageId?packageId="+unicode(assetid))
		result = []
		for part in a:
			i = a.index(part)
			b = part
			link = u"https://www.roblox.com/library/"+unicode(b)
			result.insert(i,link)
		return result

	#GET https://api.roblox.com/Ownership/HasAsset?userId={userId}&assetId={assetId}
	#Returns Boolean
	def hasAsset(userid,assetid):
		a = Http.sendRequest(u"https://api.roblox.com/Ownership/HasAsset?userId="+unicode(userid)+u"&assetId="+unicode(assetid))
		if a == u"true" or True:
			return True
		else:
			return False

	#GET https://api.roblox.com/Marketplace/ProductInfo?assetId={assetId}
	#Returns Table/Array + Attributes
	def getAssetInfo(assetid):
		c = Http.sendRequest(u"https://api.roblox.com/Marketplace/ProductInfo?assetId="+unicode(assetid))
		b = c.decode(u"utf-8")
		a = json.loads(b)
		global Asset
		Asset = lambda: None
		Asset.Name = a[u"Name"]
		Asset.Id = a[u"AssetId"]
		Asset.ProductId = a[u"ProductId"]
		Asset.Description = a[u"Description"]
		Asset.AssetTypeId = a[u"AssetTypeId"]
		Asset.CreatorName = a[u"Creator"][u"Name"]
		Asset.CreatorId = a[u"Creator"][u"Id"]
		Asset.CreatorType = a[u"Creator"][u"CreatorType"]
		Asset.CreatorTargetId = a[u"Creator"][u"CreatorTargetId"]
		Asset.IconImageAssetId = a[u"IconImageAssetId"]
		Asset.Created = a[u"Created"]
		Asset.Updated = a[u"Updated"]
		Asset.PriceInRobux = a[u"PriceInRobux"]
		Asset.Sales = a[u"Sales"]
		Asset.IsNew = a[u"IsNew"]
		Asset.IsForSale = a[u"IsForSale"]
		Asset.IsPublicDomain = a[u"IsPublicDomain"]
		Asset.IsLimited = a[u"IsLimited"]
		Asset.IsLimitedUnique = a[u"IsLimitedUnique"]
		Asset.Remaining = a[u"Remaining"]
		Asset.MinimumMembershipLevel = a[u"MinimumMembershipLevel"]
		Asset.ContentRatingTypeId = a[u"ContentRatingTypeId"]
		return Asset	

	#GET https://www.roblox.com/studio/plugins/info?assetId={assetId}
	#Returns Table/Array
	def getAssetVersions(assetid):
		a = Http.sendRequest(u"https://www.roblox.com/studio/plugins/info?assetId="+unicode(assetid))
		result = []
		for part in a:
			i = a.index(part)
			b = part
			result.insert(i,part)
		return result