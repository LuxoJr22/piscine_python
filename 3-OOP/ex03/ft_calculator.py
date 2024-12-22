class calculator:
	"""Class that is able to do calculations"""
	def __init__(self, vector):
		"""Constructor of the calculator class"""
		self.vector = vector

	def __add__(self, object) -> None:
		"""Add object to each element of vector"""
		for i in range(len(self.vector)):
			self.vector[i] = self.vector[i] + object
		print(self.vector)
		return

	def __mul__(self, object) -> None:
		"""Multiply each element of vector by object"""
		for i in range(len(self.vector)):
			self.vector[i] = self.vector[i] * object
		print(self.vector)
		return

	def __sub__(self, object) -> None:
		"""Subtract object to each element of vector"""
		for i in range(len(self.vector)):
			self.vector[i] = self.vector[i] - object
		print(self.vector)
		return

	def __truediv__(self, object) -> None:
		"""Divide each element of vector object"""
		if object == 0:
			print("Cannot divide by zero")
			return
		for i in range(len(self.vector)):
			self.vector[i] = self.vector[i] / object
		print(self.vector)
		return