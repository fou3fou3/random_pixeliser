from PIL import Image
from random import randint


def generate_pixels(size: tuple[int, int] = (100, 100)):
	# Create a new image
	img = Image.new('RGB', size)

	# Get the pixel data
	pixels = img.load()

	for x in range(0, size[0]):
		for y in range(0, size[1]):
			pixels[x, y] = (randint(0, 255), randint(0, 255), randint(0, 255))

	img.show()

