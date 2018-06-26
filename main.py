import colorama, random

colorama.init()

quit_cmd = ["q", "quit"]
look_cmd = ["l", "look"]
east_cmd = ["e", "east"]
west_cmd = ["w", "west"]
north_cmd = ["n", "north"]
south_cmd = ["s", "south"]
char_cmd = ["c", "char"]

# List of D&D alignments
alignments = (
	("Lawful Good", "Neutral Good", "Chaotic Good"),
	("Lawful Neutral", "True Neutral", "Chaotic Neutral"),
	("Lawful Evil", "Neutral Evil", "Chaotic Evil")
)

races = (
	"Human",
	"Elf",
	"Dwarf"
)

class Person:
	def __init__(self, name, location, race=None, ability_scores=None, alignment=None):
		self.name = name
		self.location = location
		
		if race is None:
			self.race = races[0]
		
		if ability_scores is None:
			self.ability_scores = [10, 10, 10, 10, 10, 10]
			
		if alignment is None:
			self.alignment = alignments[0][2]

def print_roomdata():
	print(colorama.Style.BRIGHT + world[player.location][0] + ":\n" + colorama.Style.RESET_ALL)
	print(world[player.location][1])

def print_playerstats():
	print("Player " + player.name + ":")
	print("Race:", player.race)
	print("Alignment:", player.alignment)
	
'''
World format:
(name, description, north, south, west, east)
'''

world = [
	("Test Room", "This is a test room.", 
	None, None, None, 1),
	("Another Test Room", "This is a second test room.", 
	None, None, 0, None)
]

player = Person("Bob", 0)

cmd = ""

print_roomdata()

while cmd not in quit_cmd:
	cmd = input("> ")
	
	if cmd in look_cmd:
		print_roomdata()
		
	if cmd in char_cmd:
		print_playerstats()
		
	if cmd in east_cmd and world[player.location][5] is not None:
		player.location = world[player.location][5]
		print_roomdata()
		
	if cmd in west_cmd and world[player.location][4] is not None:
		player.location = world[player.location][4]
		print_roomdata()
	
	if cmd in north_cmd and world[player.location][2] is not None:
		player.location = world[player.location][2]
		print_roomdata()

	if cmd in south_cmd and world[player.location][3] is not None:
		player.location = world[player.location][3]
		print_roomdata()