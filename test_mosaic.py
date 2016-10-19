from PIL import Image
import numpy as np
from mosaic import *
from nearest_neighbor import *

def main():
	img = np.zeros((100,100,3), np.uint8)
	img[0:100,0:100,0:3] = 255
	out1 = Image.fromarray(img, 'RGB')
	out1.save("m1.png")
	bayer = mosaic_bayer(img)
	out2 = Image.fromarray(bayer, 'RGB')
	out2.save("m2.png")
	img[0:100,0:100,0:3] = 255
	xtrans = mosaic_xtrans(img)
	out3 = Image.fromarray(xtrans, 'RGB')
	out3.save("m3.png")

if __name__ == '__main__':
	main()