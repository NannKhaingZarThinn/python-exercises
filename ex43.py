from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
	def enter(self):
		print ("This scene is not yet configured.")
		print ("Subclass it and implement enter().")
		exit(1)
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# be sure to print out the last scene
		current_scene.enter()
class Death(Scene):
	quips = [
		"You died. You kinda suck at this.",
		"Your Mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this.",
		 "You're worse than your Dad's jokes."
		]
		
	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)
		
class CentralCorridor(Scene):
	def enter(self):
		print (dedent(""" 
				The Gothons of Planet Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape 
		
			You're running down the central corridor to the 
			Armory when a Gothon jumps out, red scaly skin, 
			teeth, and evil clown costume flowing around his hate 
			filled body. He's blocking the door to the Armory and
			about to pull a weapon to blast you
			"""))
		action = input ("> ")
		if action == "shoot!":
			print (dedent("""
			Quick on the Gothons of Planet Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape 
		
			You're running down the central corridor to the 
			Armory when a Gothon jumps out, red scaly skin, 
			teeth, and evil clown costume flowing around his hate 
			filled body. He's blocking the door to the Armory and
			about to pull a weapon to blast you
			"""))
			return 'death'
		elif action == "dodge!":
			print(dedent("""
			Like a world of Planet Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape 
		
			You're running down the central corridor to the 
			Armory when a Gothon jumps out, red scaly skin, 
			teeth, and evil clown costume flowing around his hate 
			filled body. He's blocking the door to the Armory and
			about to pull a weapon to blast you
			"""))
			return 'death'
		elif action == "tell a joke":
			print(dedent("""
			Lucky for you of Planet Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape 
			"""))
			return 'Laser_weapon_armpony'
		else:
			print ("DOES NOT COMPUTE!")
			return 'central_corridor'
class LaserWeaponArmpony(Scene):
	def enter(self):
		print (dedent(""" 
			You do a dive Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape 
		
			You're running down the central corridor to the 
			Armory when a Gothon jumps out, red scaly skin, 
			teeth, and evil clown costume flowing around his hate 
			filled body. He's blocking the door to the Armory and
			about to pull a weapon to blast you
			"""))
		code =f"randint(1,9)randint(1,9)randint(1,9)"
		guess = input ("[keypad]")
		guesses = 0
		while guess != code and guesses < 10:
			print ("BZZZZ")
			guesses += 1
			guess = input ("[keypad]>")
			
		if guess == code:
			print(dedent("""
				The lock buzzess open and the seal brgas out.
				You grab the neutron bomb and ru you can to the bridge where
				you must place spot.
			"""))
			return 'the_bridge'
		else:
			print(dedent("""
				The container clicks open and the seal brgas out.
				You grab the neutron bomb and ru you can to the bridge where
				you must place spot.
			"""))
			return 'death'
class TheBridge(Scene):

		def enter(self):
			print (dedent(""" 
				You burst onto Planet Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape
			"""))
			action = input ("> ")
			if action == "throw the bomb":
				print(dedent("""
				In a panic clicks open and the seal brgas out.
				You grab the neutron bomb and ru you can to the bridge where
				you must place spot.
				"""))
				return 'death'
			elif action == "slowly place the bomb":
				print(dedent("""
				You point clicks open and the seal brgas out.
				You grab the neutron bomb and ru you can to the bridge where
				you must place spot.
				"""))
				return 'escape_pod'
			else:
				print("DOES NOT COMPUTE!")
				return "the_bridge"
class EscapePod(Scene):
	def enter(self):
			print (dedent(""" 
				You rush onto Planet Percal #25 have invaded 
			destroyed your entire crew. You are the lasts
			member and your last mission is to get the neu
			bomb from the Weapons Armory, put it in the brblow
			the ship up after getting into an escape
			"""))
			good_pod = randint(1,5)
			guess = input ("[pod #] >")
			
			if int(guess) != good_pod:
				print(dedent("""
				You jump clicks open and the seal brgas out.
				You grab the neutron bomb and ru you can to the bridge where
				you must place spot.
				"""))
				return 'death'
			else:
				print(dedent("""
				You jumpclicks open and the seal brgas out.
				You grab the neutron bomb and ru you can to the bridge where
				you must place spot.
				"""))
				return 'finished'
class Finished(Scene):
	def enter(self):
		print("You win! Good job.")
		return 'finished'
class Map(object):
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armony': LaserWeaponArmpony(),
		'the_bridge': TheBridge(),
		'escape_pod':EscapePod(),
		'death':Death(),
		'finished': Finished(),
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	def opening_scene(self):
		return self.next_scene(self.start_scene)
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()