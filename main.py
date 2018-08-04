import colorama, dice

# Initialize modules
colorama.init()

# Command alias definitions
quit_cmd = ("q", "quit")
look_cmd = ("l", "look")
east_cmd = ("e", "east")
west_cmd = ("w", "west")
north_cmd = ("n", "north")
south_cmd = ("s", "south")
up_cmd = ("u", "up")
down_cmd = ("d", "down")
char_cmd = ("c", "char")

# List of D&D alignments
alignments = (
	("Lawful Good", "Neutral Good", "Chaotic Good"),
	("Lawful Neutral", "True Neutral", "Chaotic Neutral"),
	("Lawful Evil", "Neutral Evil", "Chaotic Evil")
)

# List of D&D classes
char_classes = (
	"Barbarian",
	"Fighter"
)

# List of D&D races
races = (
	"Human",
	"Half-Elf",
	"Elf",
	"Dwarf",
	"Halfling"
)

# Experience table used for class progression
exp_table = (
	1000,
	3000,
	6000,
	10000,
	15000
)

# Base class for a character
class Character:
	def __init__(self, name, location, char_class=None, race=None, ability_scores=None, alignment=None, inventory=None):
		self.name = name
		self.location = location
		
		if char_class is None:
			self.char_class = CharacterClass(1, self)
		else: self.char_class = char_class
		
		if ability_scores is None:
			self.ability_scores = [13, 12, 12, 11, 10, 9]
		else: self.ability_scores = ability_scores
		
		if race is None:
			self.race = races[0]
		else: self.race = race
			
		if alignment is None:
			self.alignment = alignments[0][2]
		else: self.alignment = alignment
			
		if self.char_class.name == "Barbarian":
			self.age = 15 + int(dice.roll("1d4"))
		elif self.char_class.name == "Fighter":
			self.age = 15 + int(dice.roll("1d6"))
					
		if inventory is None:
			self.inventory = []
		else: self.inventory = inventory
		
	def printstats():
		print(f"Character {self.name}:")
		print(f"Age: {self.age}")
		print(f"Class: {self.char_class.name}")
		print(f"Race: {self.race}")
		print(f"Alignment: {self.alignment}")

class CharacterClass:
	def __init__(self, indx, parent, level=1, exp=0):
		self.name = char_classes[indx]
		self.parent = parent
		
		self.level = level
		self.exp = exp
	
def print_roomdata():
	print(colorama.Style.BRIGHT + world[player.location][0] + ":\n" + colorama.Style.RESET_ALL)
	print(world[player.location][1] + "\n")
	if world[player.location][2] is not None:
		print("There is an exit here, leading " + colorama.Style.BRIGHT + "north." + colorama.Style.RESET_ALL)
	if world[player.location][3] is not None:
		print("There is an exit here, leading " + colorama.Style.BRIGHT + "south." + colorama.Style.RESET_ALL)
	if world[player.location][4] is not None:
		print("There is an exit here, leading " + colorama.Style.BRIGHT + "west." + colorama.Style.RESET_ALL)
	if world[player.location][5] is not None:
		print("There is an exit here, leading " + colorama.Style.BRIGHT + "east." + colorama.Style.RESET_ALL)
	if world[player.location][6] is not None:
		print("There is an exit here, leading " + colorama.Style.BRIGHT + "up." + colorama.Style.RESET_ALL)
	if world[player.location][7] is not None:
		print("There is an exit here, leading " + colorama.Style.BRIGHT + " down." + colorama.Style.RESET_ALL)

# Descriptions used for multiple rooms
oldskullinntaproom_desc = "The tap room of the Old Skull Inn is, for many adventurers like yourself, one of the first images that come to mind when thinking of Shadowdale.\
\nRight now, there appears to be no one here besides yourself - but that is bound to change sometime soon."

thenorthride_desc = "The Northride passes through Shadowdale and extends all the way to the Moonsea coast."

nearweregrundthetradersshop_desc = ""

nearhammerhandswoodworking_desc = ""

shadowdaletrail_desc = ""

nearreedosulcarshouse_desc = ""

'''
Room definition format:
(name, description,
 north, south, west, east, up, down,
 objects)
'''

# Room definitions
world = [

	#0
	("Old Skull Inn Tap Room", oldskullinntaproom_desc, 
	None, 3, 2, 1, None, None,
	[]),
	
	#1
	("Old Skull Inn East Tap Room", oldskullinntaproom_desc,
	None, None, 0, None, None, None,
	[]),
	
	#2
	("Old Skull Inn West Tap Room", oldskullinntaproom_desc,
	None, None, None, 0, None, None,
	[]),
	
	#3
	("In Front of the Old Skull Inn", "",
	0, 4, 9, 6, None, None,
	[]),
	
	#4
	("The Northride", thenorthride_desc,
	3, 7, 8, 5, None, None,
	[]),
	
	#5
	("The Northride", thenorthride_desc,
	6, None, 4, 10, None, None,
	[]),
	
	#6
	("Old Skull Inn Message Post", "",
	None, 5, None, None, None, None,
	[]),
	
	#7
	("In Front of Hammerhand's Woodworking", nearhammerhandswoodworking_desc,
	4, None, 20, None, None, None,
	[]),
	
	#8
	("The Northride", thenorthride_desc,
	9, 7, 18, 4, None, None,
	[]),
	
	#9
	("In Front of Miera Lulhannon's House", "",
	None, 8, 19, 3, None, None,
	[]),
	
	#10
	("The Northride", thenorthride_desc,
	None, 11, 5, None, None, None,
	[]),
	
	#11
	("In Front of Weregrund the Trader's Shop", nearweregrundthetradersshop_desc,
	10, None, 12, None, None, None,
	[]),
	
	#12
	("West of Weregrund the Trader's Shop", nearweregrundthetradersshop_desc,
	None, 14, 13, 11, None, None,
	[]),
	
	#13
	("East of Hammerhand's Woodworking", nearhammerhandswoodworking_desc,
	None, None, 7, 12, None, None,
	[]),
	
	#14
	("South of Weregrund the Trader's Shop", nearweregrundthetradersshop_desc,
	12, 15, 13, None, None, None,
	[]),
	
	#15
	("The Shadowdale Trail", shadowdaletrail_desc,
	14, None, None, 16, None, None,
	[]),
	
	#16
	("East of Reedo Sulcar's House", nearreedosulcarshouse_desc,
	17, None, 15, None, None, None,
	[]),
	
	#17
	("East of Weregrund the Trader's Shop", nearweregrundthetradersshop_desc,
	25, 16, None, None, None, None,
	[]),
	
	#18
	("The Northride", thenorthride_desc,
	19, 20, 21, 8, None, None,
	[]),
	
	#19
	("In Front of Jamble the Eye's House", "",
	None, 18, None, 9, None, None,
	[]),
	
	#20
	("In Front of Latha Brannon's Boardinghouse", "",
	18, None, 22, 7, None, None,
	[]),
	
	#21
	("The Northride", thenorthride_desc,
	22, 23, 24, 18, None, None,
	[]),
	
	#22
	("In Front of a Stone House", "",
	None, 21, None, 20, None, None,
	[]),
	
	#23
	("In Front of Hoareb Nimblefingers' House", "",
	21, None, None, 20, None, None,
	[]),
	
	#24
	("The Northride", thenorthride_desc,
	None, None, None, 21, None, None,
	[]),
	
	#25
	("The Northride", thenorthride_desc,
	None, 17, 5, None, None, None,
	[])
	
	#26
]

player = Character("Bob", 0)

# Print introduction message
print("Welcome to the Forgotten Realms RPG by Addemup, currently made with a world of " + str(len(world)) + " rooms.\n")

# Initial setup of the game
cmd = ""

print_roomdata()

# Command interpretation
while cmd not in quit_cmd:
	cmd = input("> ")
	
	if cmd in look_cmd:
		print_roomdata()
	elif cmd in char_cmd:
		player.printstats()
	elif cmd in east_cmd and world[player.location][5] is not None:
		player.location = world[player.location][5]
		print_roomdata()
	elif cmd in west_cmd and world[player.location][4] is not None:
		player.location = world[player.location][4]
		print_roomdata()
	elif cmd in north_cmd and world[player.location][2] is not None:
		player.location = world[player.location][2]
		print_roomdata()
	elif cmd in south_cmd and world[player.location][3] is not None:
		player.location = world[player.location][3]
		print_roomdata()
	elif cmd in up_cmd and world[player.location][6] is not None:
		player.location = world[player.location][6]
		print_roomdata()
	elif cmd in down_cmd and world[player.location][7] is not None:
		player.location = world[player.location][7]
		print_roomdata()
	else:
		if cmd not in quit_cmd:
			print("Command '" + cmd + "' not found.")
