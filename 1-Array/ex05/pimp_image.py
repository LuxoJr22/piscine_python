from PIL import Image
import numpy as np

def ft_invert(array) -> list:
	"""Inverts the color of the image received."""
	img = np.array(array, copy=True)
	for i in img:
		for x in i:
			x[0] = 255 - x[0]
			x[1] = 255 - x[1]
			x[2] = 255 - x[2]
	Image.fromarray(img, "RGB").show()
	return

def ft_red(array) -> list:
	"""Get only red value of the image received."""
	img = np.array(array, copy=True)
	for i in img:
		for x in i:
			x[0] = x[0]
			x[1] = 0
			x[2] = 0
	Image.fromarray(img, "RGB").show()
	return

def ft_green(array) -> list:
	"""Get only green value of the image received."""
	img = np.array(array, copy=True)
	for i in img:
		for x in i:
			x[0] = 0
			x[1] = x[1]
			x[2] = 0
	Image.fromarray(img, "RGB").show()
	return

def ft_blue(array) -> list:
	"""Get only blue value of the image received."""
	img = np.array(array, copy=True)
	for i in img:
		for x in i:
			x[0] = 0
			x[1] = 0
			x[2] = x[2]
	Image.fromarray(img, "RGB").show()
	return

def ft_grey(array) -> list:
	"""Convert image as black and white."""
	Image.fromarray(array, "RGB").convert('L').show()
	return

