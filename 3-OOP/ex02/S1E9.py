from abc import ABC, abstractmethod

class Character(ABC):
	"""Abstract class that define a character with a name and a health state"""
	@abstractmethod
	def __init__(self, first_name, alive=True):
		"""Constructor of the character class"""
		self.first_name = first_name
		self.is_alive = alive

	def die(self):
		"""Change is_alive value to false"""
		self.is_alive = False
	


#your code here
class Stark(Character):
	"""Character class that inherit from Character"""
	def __init__(self, first_name, alive=True):
		"""Constructor of the Stark class"""
		super().__init__(first_name, alive)