import imageio as iio
import numpy as np

def ft_load(path: str) -> list:
	"""Loads an image, prints its format, and return its pixels
	content in RGB format"""
	try:
		img = iio.imread(path)
		return (img)
	except FileNotFoundError:
		print("The file doesn't exist")
	except PermissionError:
		print("Permission needed to open this file")
	except ValueError:
		print("Can't open this file")