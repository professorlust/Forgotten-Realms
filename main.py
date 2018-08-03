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

def print_playerstats():
	print(f"Character {player.name}:")
	print(f"Age: {player.age}")
	print(f"Class: {player.char_class.name}")
	print(f"Race: {player.race}")
	print(f"Alignment: {player.alignment}")
	
'''
Room format:
(name, description,
 north, south, west, east, up, down)
'''

oldskullinntaproom_desc = "The tap room of the Old Skull Inn is, for many adventurers like yourself, one of the first images that come to mind when thinking of Shadowdale.\
\nRight now, there appears to be no one here besides yourself - but that is bound to change sometime soon."

# Room definitions
world = [
	("Old Skull Inn Tap Room", oldskullinntaproom_desc, 
	None, 3, 2, 1, None, None),
	("Old Skull Inn East Tap Room", oldskullinntaproom_desc,
	None, None, 0, None, None, None),
	("Old Skull Inn West Tap Room", oldskullinntaproom_desc,
	None, None, None, 0, None, None),
	("In Front of the Old Skull Inn", "",
	0, 4, 9, 6, None, None),
	("The Northride", "",
	3, 7, 8, 5, None, None),
	("The Northride", "",
	6, None, 4, None, None, None),
	("Old Skull Inn Message Post", "",
	None, 5, None, None, None, None),
	("In Front of Hammerhand's Woodworking", "",
	4, None, None, None, None, None),
	("The Northride", "",
	9, None, None, 4, None, None),
	("In Front of Miera Lulhannon's House", "",
	None, 8, None, 3, None, None)
]

player = Character("Bob", 0)

print("Welcome to the Forgotten Realms RPG, with a world currently made of " + str(len(world)) + " rooms.\n")

cmd = ""

print_roomdata()

while cmd not in quit_cmd:
	cmd = input("> ")
	
	if cmd in look_cmd:
		print_roomdata()
	elif cmd in char_cmd:
		print_playerstats()
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
