def square(x: int | float) -> int | float:
	"""Return square of argument"""
	return x * x

def pow(x: int | float) -> int | float:
	"""Return exponentiation of argument by itself"""
	return x**x

def outer(x: int | float, function) -> object:
	"""A function that takes as argument a number and a function and returns 
	an object that when called returns the result of the arguments calculation."""
	count = 0
	def inner() -> float:
		"""Apply the function passed as argument to the outer function to the x"""
		nonlocal x
		nonlocal count
		count += 1
		x = function(x)
		return x
	return inner