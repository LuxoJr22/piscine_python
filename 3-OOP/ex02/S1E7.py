from S1E9 import Character
class Baratheon(Character):
	"""Representing the Baratheon family"""
	def __init__(self, first_name, alive=True):
		"""Constructor of the Baratheon class"""
		super().__init__(first_name, alive)
		self.family_name = 'Baratheon'
		self.eyes = 'brown'
		self.hairs = 'dark'

	def __str__(self):
		"""Return string representation of the class"""
		return (f'Vector: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')')
	
	def __repr__(self):
		"""Return string representation of the class"""
		return (f'Vector: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')')

class Lannister(Character):
	"""Representing the Lannister family"""
	def __init__(self, first_name, alive=True):
		"""Constructor of the Lannister class"""
		super().__init__(first_name, alive)
		self.family_name = 'Lannister'
		self.eyes = 'blue'
		self.hairs = 'light'

	@staticmethod
	def create_lannister(name, alive=True):
		"""Create an instance of Lannister"""
		return Lannister(name, alive)
	
	def __str__(self):
		"""Return string representation of the class"""
		return (f'Vector: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')')
	
	def __repr__(self):
		"""Return string representation of the class"""
		return (f'Vector: (\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')')
