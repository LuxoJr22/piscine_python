def callLimit(limit: int):
	"""Return the limiter object"""
	count = 0
	def callLimiter(function):
		"""Object that call the limiter"""
		def limit_function(*args: any, **kwds: any):
			"""Call the function and apply the limit"""
			nonlocal count
			if (count < limit):
				function()
				count += 1
			else:
				print("Error:", function, "call too many times")
		return(limit_function)
	return(callLimiter)
