from load_image import ft_load
from PIL import Image
import numpy as np

def main():
	img = ft_load("animal.jpeg")
	print(img)
	sliced = img[slice(0, 400)]
	go = Image.fromarray(sliced, "RGB").convert('L')
	print(f"New shape after slicing : {np.shape(go)}")
	go.save("saved.jpg")
	return


if __name__ == "__main__":
    main()