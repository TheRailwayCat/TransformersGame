#Python Test RPG
#Caroline (CRL) Ruth Lewis
#This will be AWESOMEEEE!!!!!

import cmd
import textwrap
import sys
import os
import time
import random
import traceback

screen_width = 100

#### Player Setup ####
#I think I'll make a game where SunWuKong is fighting all his enemies
#Just an idea
# Nope I will makw it transformers


class player:
	def __init__(self):
		self.name = 'Barry'
		self.job = '1'
		self.hp = 0
		self.fp = 0
		self.status_effects = []
		self.location = 'S1'
		self.game_over = False

myPlayer = player()

#### Title Screen ####
def title_screen_selections():
	choices = ['play', 'help', 'quit']
	while True:
		print(f"Select option: {", ".join(sorted(choices))}")
		option = input(">")
		if option.lower() == ("play"):
			setup_game()
			break
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()
		print("Error; please enter a valid command")
yes = ['yes','y']
no = ['no','n']
yesno = ['yes','y','no','n']
def title_screen():
	os.system('cls')
	print('###########################')
	print('#                         #')
	print('# Welcome to the Text RPG #')
	print('#                         #')
	print('###########################')
	print('          -Play-           ')
	print('          -Help-           ')
	print('          -Quit-           ')
	title_screen_selections()

def help_menu():
	os.system('cls')
	print('###########################')
	print('#                         #')
	print('# Welcome to the Text RPG #')
	print('#                         #')
	print('###########################')
	print('-help opens the help menu')
	print('-quit allows you to leave')
	print('-play allows you to start the game')
	print('-Good luck and have fun')
	title_screen_selections()


#### Map ###
"""
Player starts in S1

 X    --------
------|  S4  |-----
|  |  |  XO  | S5 |
|S2|S3|      |   X|
|------      -----|
|				  |
|		S1		  |
|	      --------|
|	      | | |X| |
-------------------
   H
--------
|  S6  |
|     x|
--------
"""

# ZONENAME: ""
# DESCRIPTION: "description"
# EXAMINATION: "examniation"
# LOCKED: False
# MONSTER: False
# ENERGON: False

locked_places = {'S1': False, 'S2': False, 'S3': False,
 'S4': False, 'S5': True, 'S6': True}
 
### Making the map
zonemap = {
	'S1': {
		'ZONENAME': "the Central Sector" ,
		'DESCRIPTION': "There are 2 cells to the left a large transport section a large cell to the right on the other side there are desks and some storage cabinets",
		'EXAMINATION': "examniation",
		'LOCKED': False ,
		'MONSTER': False ,
		'ENERGON': True,
		},
	'S2':{
		'ZONENAME': "Cell #1" ,
		'DESCRIPTION': "A small cell with a organic squishy very acidic alien corpse which was stabbed with alien rock which came through a hole in the wall",
		'EXAMINATION': "examniation",
		'LOCKED': False ,
		'MONSTER': False ,
		'ENERGON': True ,
		},
	'S3':{
		'ZONENAME': "Cell #2",
		'DESCRIPTION': "A small cell with a skull and some bones and a keyring with only one key hiding in the skeleton's hand",
		'EXAMINATION': "examniation",
		'LOCKED': False ,
		'MONSTER': False ,
		'ENERGON': False ,
		},
	'S4':{
		'ZONENAME': "the Transporter Lab",
		'DESCRIPTION': "A circular transport machine which has frayed wires exposed panels and such. In the back there is some computers which seem a little old fashioned. There is a large lever which turns on the power and it wont work but sparks go everywhere. there is a piece of energon beneath the machine",
		'EXAMINATION': "examniation",
		'LOCKED': False ,
		'MONSTER': False ,
		'ENERGON': True ,
		},
	'S5':{
		'ZONENAME': "Cell #3" ,
		'DESCRIPTION': "A larger cell with a large aggressive part organic part technology wormlike beast which is guarding the energon in the middle of the room",
		'EXAMINATION': "examniation",
		'LOCKED': True ,
		'MONSTER': True ,
		'ENERGON': True ,
		},
	'S6':{
		'ZONENAME': "the Hidden Room" ,
		'DESCRIPTION': "A room with a similar acidic organic corpse but this one has an energon crystal which brings an energon ghost of an insectoid alien which looks up at you surprised",
		'EXAMINATION': "examniation",
		'LOCKED': False ,
		'MONSTER': True ,
		'ENERGON': True ,
		},}

####Game Interactivity
def print_location():
	print('\n' + ('#'*(10 + len(zonemap[myPlayer.location]['ZONENAME']))))
	print('#    ' + zonemap[myPlayer.location]['ZONENAME'] + '    #')
	print('# ' + textwrap.fill(zonemap[myPlayer.location]['DESCRIPTION'], len(zonemap[myPlayer.location]['ZONENAME']) + 8) + ' #')
	print('\n' + ('#'*(10 + len(zonemap[myPlayer.location]['ZONENAME']))))
#Above is just making it look nice
def prompt():
	acceptable_actions = ['move', 'go', 'travel', 'walk','quit','exit','q','examine', 'inspect', 'interact', 'look', 'where am i', 'list']
	Gen_Text = "What would you like to do? ('list' to list commands)"
	
	print("\n" + '='*(len(Gen_Text)))
	print(Gen_Text)
	print('='*(len(Gen_Text)) + '\n')
	#Above is just looking nice
	action = input(">")
	while action.lower() not in acceptable_actions:
			print("Unknown prompt action try again.\n")
			action = input(">")
	if action.lower() in ['quit', 'exit','q']:
		sys.exit()#player quit
	elif action.lower() == 'list':
		print(f"Commands: {", ".join(acceptable_actions)}")
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		player_move(action.lower())
	elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
		player_examine(action.lower())
	elif action.lower() in ['where am i']:
		print("You are in the " + zonemap[myPlayer.location]['ZONENAME'] + ".")

def player_move(myAction):
	if myPlayer.location == 'S1':
		print("\nWhere would you like to go? You could go in one of the cells,\nin the transporter room, or just check out the storage units in the corner.\n\n1)One of the cells 2) transporter room 3) storage units\n")
		dest = input(">")
		if dest.lower() in ['1', 'cells']:
			print("\nWhich cell would you like to enter: 1, 2, or 3?\n")
			cellnum = input(">")
			if cellnum.lower() in ['1', 'cell 1']:
				destination = 'S2'
				movement_handler(destination)
			elif cellnum.lower() in ['2', 'cell 2', 'Cell 2']:
				destination = 'S3'
				movement_handler(destination)
			elif cellnum.lower() in ['3', 'cell 3', 'Cell 3']:
				destination = 'S5'
				movement_handler(destination)
		elif dest.lower() in ['2', 'transporter room']:
			destination = 'S4'
			movement_handler(destination)
		elif dest.lower() in ['3', 'storage units']:
			print("chests here")
		else:
			print("That's not a place.")
			prompt()
			#This above is moving when you are in the central room
	elif myPlayer.location in ['S2','S3','S4','S5','S6']:
		print("\nWould you like to exit this room? y/n\n")
		exitroom = input(">")
		while exitroom.lower() not in yesno:
			print("Unknown exit action try again.")
			prompt()
		if exitroom.lower() in yes:
			destination = 'S1'
			movement_handler(destination)
		elif exitroom.lower() in no:
			return
	else:
		print("Where the F*** are you? Something's wrong")

def movement_handler(destination):
	if zonemap[destination]['LOCKED']:
		print("\n"+"The door is locked. You might need a key.")
		prompt()
	else:
		print("\n" + "You have moved to " + zonemap[destination]['ZONENAME'] + ".")
		myPlayer.location = destination
		print_location()

def player_examine(action):
	if zonemap[myPlayer.location]['ENERGON']:
		print("You have already discovered the secrets here")
	else:
		print("You can explore here if you want")

#### Game Functionailty ####

def main_game_loop():
	while myPlayer.game_over == False:
		prompt()
#Aparently here is for if puzzles have been solved monsters defeated etc.

def display_speech(speech, delay=0.02):
	for character in speech:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(delay)

def setup_game():
	os.system('cls')

 #### Name collecting ####
	display_speech("Hello, what's your name?\n", 0.05)
	player_name = input(">")
	myPlayer.name = player_name
	while True:
		display_speech(player_name + ", is that right? y/n\n")
		response_name = input(">")
		if response_name.lower() in yes:
			myPlayer.name = player_name
			break
		elif response_name.lower() in no:
			print("Okay, what's your name, then?")
			player_name = input(">")
			myPlayer.name = player_name
		elif response_name.lower() not in yesno:
			print("Unknown name action try again.")

 #### Job handling ####
	display_speech("Lovely name, what's your job?\n", 0.05)
	display_speech("(You can be a 1, 2, or 3.)\n", 0.05)
	valid_jobs = {
		'1': (120, 20),
		'2': (40, 100),
		'3': (80, 60)
	}

	while True:
		player_job = input(">")
		if player_job.lower() in valid_jobs:
			myPlayer.job = player_job.lower()
			myPlayer.hp, myPlayer.fp = valid_jobs[myPlayer.job]
			break
		else:
			print(f"Silly that's not a job; valid jobs are {sorted(valid_jobs.keys())}")
		
	print("Excellent, I am sure you will make a wonderful " + player_job + ".\n")

	####Introduction
	display_speech("Welcome, " + player_name + " the " + player_job + ".\n", 0.05)
	display_speech("Welcome to the wonderful city of Borgefell.\n", 0.02)
	display_speech("It's a lovely city with many lovely places.\n", 0.04)
	display_speech("And no crime problem.\n", 0.03)
	display_speech("Just stay in the planned districts.\n", 0.02)
	display_speech(".....", 0.05)

	os.system('cls')
	print("########################")
	print("#  Let's get started!  #")
	print("########################")
	main_game_loop()

####Starting the program####
try:
	title_screen()
except Exception:
	print(f"EXCEPTION:")
	print(traceback.format_exc())

time.sleep(300)
