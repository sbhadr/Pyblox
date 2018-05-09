from .libs.colors import *

class Logging:

	def Error(message):
		print red("Pyblox | Error | "+message)

	def Warning(message):
		print yellow("Pyblox | Warning | "+message)

	def Success(message):
		print green("Pyblox | Success | "+message)

	def Log(message):
		print white("Pyblox | Info | "+message)