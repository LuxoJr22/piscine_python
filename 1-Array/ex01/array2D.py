import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""Takes as parameters a 2D array, prints its shape, and returns a
	truncated version of the array based on the provided start and end arguments."""
	if (len(np.shape(family)) != 2):
		print("Must be a 2D array")
		return []
	print(f"My shape is : {np.shape(family)}")
	sliced = family[slice(start, end)]
	print(f"My new shape is : {np.shape(sliced)}")
	return sliced