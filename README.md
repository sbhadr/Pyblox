# roblox.py

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()

An API wrapper for Roblox written in Python.

The purpose of this API wrapper is to expose Roblox's API for third party use and/or for individual standalone projects.
This is the first stable API wrapper for the Roblox API. If you would like to contribute, create a pull request will the changes you made. If you have a complaint, issue or problem, create an issue and I will try to answer as fast as I can. 

### Updating

The Roblox API updates whenever nessary and often the developers don't specify when or why these changes are taking place.
Due to this, this repo could break at anytime. If a break does occur, please open up an issue on this repo.

## Installing

To install roblox.py to your windows machine, you must do the following:
```
1. Download or Clone this repo
2. Place the "roblox" folder into C:\Users\YOURUSERNAMEONWINDOWSMACHINE\AppData\Local\Programs\Python\Python35-32\Lib\site-packages
```
MacOS and Linux are supported but installation will vary.
This was developed on a windows-based machine and thus, it's recommended to use windows.

## Quick Example

```py
from roblox import * # Imports the API Wrapper 

def haha():
	CoolPeople = Friends.friendList(1) # Gets Friends List
	print(CoolPeople) # Returns usernames and prints them on console

haha() # Calls "haha" method
```

## Requirements

- Python 3.5+
- ``pip install requests``

*note: requests may have been already installed*

## Related Projects
N/A
