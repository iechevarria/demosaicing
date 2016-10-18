""" Use nearest neighbor algorithm to replace channel information """

from PIL import Image
import numpy as np

def nn_demosaic_bayer(img, x_offset = 0, y_offset = 0):
	""" Replaces channel information by taking the nearest neighbor's value """

	for i in range(int(img.shape[0])):
		dy = (i + y_offset) % 2
		for j in range(int(img.shape[1])):
			dx = (j + x_offset) % 2

			# blue/green row
			if dy == 0: 
				# green: replace red and blue 
				if dx == 0:
					if i + 1 < int(img.shape[0]):
						img[i][j][0] = img[i+1][j][0]
					else:
						img[i][j][0] = img[i-1][j][0]
					if j + 1 < int(img.shape[1]):
						img[i][j][2] = img[i][j+1][2]
					else:
						img[i][j][2] = img[i][j-1][2]

				# blue: replace green and red
				else:
					if i + 1 < int(img.shape[0]):
						img[i][j][1] = img[i+1][j][1]
					else:
						img[i][j][1] = img[i-1][j][1]
					if i + 1 < int(img.shape[0]) and j + 1 < int(img.shape[1]):
						img[i][j][0] = img[i+1][j+1][0]
					else:
						img[i][j][0] = img[i-1][j-1][0]

			# red/green row
			else:
				# red: replace green and blue 
				if dx == 0:
					if i + 1 < int(img.shape[0]):
						img[i][j][1] = img[i+1][j][1]
					else:
						img[i][j][1] = img[i-1][j][1]
					if i + 1 < int(img.shape[0]) and j + 1 < int(img.shape[1]):
						img[i][j][2] = img[i+1][j+1][2]
					else:
						img[i][j][2] = img[i-1][j-1][2]

				# green: replace red and blue 
				else:
					if j + 1 < int(img.shape[0]):
						img[i][j][0] = img[i][j+1][0]
					else:
						img[i][j][0] = img[i][j-1][0]
					if i + 1 < int(img.shape[1]):
						img[i][j][2] = img[i+1][j][2]
					else:
						img[i][j][2] = img[i-1][j][2]

	return img


def nn_demosaic_xtrans(img, x_offset, y_offset):
	""" Replaces channel information by taking the nearest neighbor's value """
	return


def main():
	from remosaic import to_bayer
	img = Image.open("sample.jpg")
	img = np.asarray(img)
	img.flags.writeable = True
	out1 = Image.fromarray(img, 'RGB')
	out1.save("nn1.png")
	img = to_bayer(img)
	out2 = Image.fromarray(img, 'RGB')
	out2.save("nn2.png")
	img = nn_demosaic_bayer(img)
	out3 = Image.fromarray(img, 'RGB')
	out3.save("nn3.png")


if __name__ == '__main__':
	main()