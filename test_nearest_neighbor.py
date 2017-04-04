from PIL import Image
import numpy as np
from mosaic import *
from nearest_neighbor import *

def main():
	img = Image.open("samples/sample.jpg")
	img = np.asarray(img)
	img.flags.writeable = True
	out1 = Image.fromarray(img, 'RGB')
	out1.save("original.png")
	img = mosaic_bayer(img)
	out2 = Image.fromarray(img, 'RGB')
	out2.save("mosaic.png")
	img = nnd_bayer(img)
	out3 = Image.fromarray(img, 'RGB')
	out3.save("nearestneighbor.png")

if __name__ == '__main__':
	main()