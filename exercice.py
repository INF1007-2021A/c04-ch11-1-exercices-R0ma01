"""
Chapitre 11.1
"""


import math
from inspect import *

from game import *

class Character:

	def __init__(self, name, max_hp, attack, defence, level) -> None:
		self._name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defence = defence
		self.level = level
		self.hp = max_hp
		self.weapon = None
		

class Weapon:

	def __init__(self, name, damage, level) -> None:
		self.name = name
		self.damage = damage
		self.usage = level

	@classmethod

	def make_unarmed():
		Weapon.name = "Unarmed"
		Weapon.damage = 20
		Weapon.usage = 0 
		

def run_battle(c1, c2):

	while c1.hp > 0 and c2.hp >0:
		c1.hp  -= c2.attack
		c2.hp -= c1.attack
		pass

	



	


def main():
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmor", 250, 100, 120, 60)

	print (c1.hp)

	print (c2.hp)
	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	print (c1.weapon.name)
	#turns = run_battle(c1, c2)
	#print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

