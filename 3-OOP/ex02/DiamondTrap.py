from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""Representing the king"""
	def __init__(self, first_name, alive=True):
		"""Constructor of the king class"""
		super().__init__(first_name, alive)

	def set_eyes(self, color):
		"""Set eye color"""
		self.eyes = color
	
	def set_hairs(self, color):
		"""Set hair color"""
		self.hairs = color

	def get_eyes(self):
		"""Return eye color"""
		return self.eyes
	
	def get_hairs(self):
		"""Return hair color"""
		return self.hairs