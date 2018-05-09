from .api.auth import Auth
from .logging import Logging
import asyncio

class Client:

	def create():
		if Auth.login(Credentials["Login"],Credentials["Password"]) == True:
			# Create some sort of Async here
			exit()
		else:
			Logging.Error("Username or Password is incorrect")
			exit()

	def exit():
		Auth.logout()
		exit()