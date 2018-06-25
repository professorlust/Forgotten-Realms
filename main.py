import colorama

colorama.init()

quit_cmd = ["q", "quit"]
look_cmd = ["l", "look"]
east_cmd = ["e", "east"]
west_cmd = ["w", "west"]

class Person:
	def __init__(self, name, location):
		self.name = name
		self.location = location

def print_roomdata():
	print(colorama.Style.BRIGHT + world[player.location][0] + ":\n" + colorama.Style.RESET_ALL)
	print(world[player.location][1])
	
'''
World format:
(name, description, north, south, west, east)
'''

world = [
	("Test Room", "This is a test room.", None, None, None, 1),
	("Another Test Room", "This is a second test room.", None, None, 0, None)
]

player = Person("Bob", 0)

cmd = ""

print_roomdata()

while cmd not in quit_cmd:
	cmd = input("> ")
	
	if cmd in look_cmd:
		print_roomdata()
		
	if cmd in east_cmd and world[player.location][5] is not None:
		player.location = world[player.location][5]
		print_roomdata()
		
	if cmd in west_cmd and world[player.location][4] is not None:
		player.location = world[player.location][4]
		print_roomdata()