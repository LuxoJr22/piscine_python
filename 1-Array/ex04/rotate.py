from load_image import ft_load
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def main():
	"""Program that load animal.jpeg print size on both axis, number of channel and pixel content of a square in the image
	before rotating the result, print the same info for the rotated image and show it"""

	img = ft_load("animal.jpeg")
	
	img =  Image.fromarray(img, "RGB").convert('L')

	crop = (400, 400)
	left = 450
	top = 100
	im = img.crop((left, top, crop[0]+left, crop[1] + top))
	print(f"The shape of image is : {np.shape(im)}")
	print(np.asarray(im))
	im = im.transpose(Image.ROTATE_90)
	
	print(f"New shape after Transpose : {np.shape(im)}")
	print(np.asarray(im))
	imgplot = plt.imshow(im, cmap='gray')
	plt.show()
      
	return


if __name__ == "__main__":
    main()