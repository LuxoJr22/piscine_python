from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
	"""Loads an image, prints its format, and return its pixels
	content in RGB format"""
	try:
		img = Image.open(path)
		print(f"The shape of image is: {np.shape(img)}")
		print(np.asarray(img))
		img.show()
		return (np.asarray(img))
	except FileNotFoundError:
		print("The file doesn't exist")
	except PermissionError:
		print("Permission needed to open this file")
	except ValueError:
		print("Can't open this file")