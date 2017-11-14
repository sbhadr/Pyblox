# Pyblox

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()
[![ROBLOX API Discord](https://img.shields.io/badge/discord-roblox%20api%20chat-blue.svg)](https://discord.gg/EDXNdAT)

An API wrapper for Roblox written in Python.

The purpose of this API wrapper is to expose Roblox's API for third party use and/or for individual standalone projects.
This is the first stable Python API wrapper for the Roblox API. Documentation can be found within each module. I encourage
developers to look into the codebase to better understand this wrapper and what it can truly offer. 

If you would like to contribute, create a pull request with the changes you made. If you have a complaint, issue or problem, create an issue and I will try to answer as fast as I can. 

### Updating

The Roblox API updates whenever nessary and often the developers don't specify when or why these changes are taking place.
Due to this, this repo could break at anytime. If a break does occur, please open up an issue on repo detailing the error.

## Installing

To install Pyblox to your windows machine, you must do the following:
```
1. Download or Clone this repo
2. Place the "pyblox" folder into C:\Users\YOURUSERNAMEONWINDOWSMACHINE\AppData\Local\Programs\Python\Python35-32\Lib\site-packages
```
MacOS and Linux are supported but installation will vary.
This was developed on a windows-based machine and thus, it's recommended to use windows.

## Quick Example

```py
import pyblox # Imports the API Wrapper 

def GetAllFriends():
	CoolPeople = Friends.friendList(1) # Gets Friends List
	print(CoolPeople) # Returns usernames and prints them on console

GetAllFriends() # Calls "GetAllFriends" method
```

## Requirements

- Python 3+
- ``pip install requests``

*note: requests may have been already installed.*
*pyblox may be compatible with python 2x. However, it has not been tested.*

## Related Projects
https://github.com/sentanos/roblox-js
https://github.com/CrescentCode/RobloxCommunication
https://github.com/CrescentCode/Freya
https://github.com/NoahCristino/robloxlib
https://github.com/winfamy/nodeblox
https://github.com/gamenew09/RobloxAPI
https://github.com/NevermoreFramework/Nevermore
