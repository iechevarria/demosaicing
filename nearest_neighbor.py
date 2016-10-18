""" Use nearest neighbor algorithm to replace channel information """

from PIL import Image
import numpy as np

def nn_demosaic_bayer(img, x_offset = 0, y_offset = 0):
	""" Replaces channel information by taking the nearest neighbor's value """

	for i in range(int(img.shape[0])):
		y = i + y_offset
		for j in range(int(img.shape[1])):
			x = j + x_offset
			dy = y % 2
			dx = x % 2

			# blue/green row
			if dy == 0: 
				# green: replace red and blue 
				if dx == 0:
					try:
						img[i][j][0] = img[i+1][j][0]
						img[i][j][2] = img[i][j+1][2]
					except:
						img[i][j][0] = img[i-1][j][0]
						img[i][j][2] = img[i][j-1][2]
				# blue: replace green and red
				else:
					try:
						img[i][j][0] = img[i+1][j+1][0]
						img[i][j][1] = img[i+1][j][1]
					except:
						img[i][j][0] = img[i-1][j-1][0]
						img[i][j][1] = img[i-1][j][1]

			# red/green row
			else:
				# red: replace green and blue 
				if dx == 0:
					try:
						img[i][j][1] = img[i+1][j][1]
						img[i][j][2] = img[i+1][j+1][2]
					except:
						img[i][j][1] = img[i-1][j][1]
						img[i][j][2] = img[i-1][j-1][2]
				# green: replace red and blue 
				else:
					try:
						img[i][j][0] = img[i+1][j][0]
						img[i][j][2] = img[i][j+1][2]
					except:
						img[i][j][0] = img[i-1][j][0]
						img[i][j][2] = img[i][j-1][2]

	return img



def nn_demosaic_xtrans(img, x_offset, y_offset):
	""" Replaces channel information by taking the nearest neighbor's value """
	return


def main():
	from remosaic import to_bayer
	print("Basic Pattern Test")
	img = np.zeros((10,10,3), np.uint8)
	img[0:100,0:100,0:3] = 255
	out1 = Image.fromarray(img, 'RGB')
	out1.save("nn1.png")
	img = to_bayer(img)
	out2 = Image.fromarray(img, 'RGB')
	out2.save("nn2.png")
	img = nn_demosaic_bayer(img)
	print(img)
	out3 = Image.fromarray(img, 'RGB')
	out3.save("nn3.png")


if __name__ == '__main__':
	main()