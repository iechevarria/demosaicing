""" Use nearest neighbor algorithm to replace channel information """

from PIL import Image
import numpy as np

def nnd_bayer(img, x_offset = 0, y_offset = 0):
	""" Replaces channel information by taking the nearest neighbor's value
		Assumption: img dimensions are divisible by 2
		TODO add offsets back in """

	for i in xrange(0, int(img.shape[0]), 2):
		for j in xrange(0, int(img.shape[1]), 2):

			# replace red values
			img[i][j][0] = img[i][j+1][0] = img[i+1][j+1][0] = img[i+1][j][0]
			# replace blue values
			img[i][j][2] = img[i+1][j][2] = img[i+1][j+1][2] = img[i][j+1][2]
			# replace green values
			img[i][j+1][1] = img[i][j][1]
			img[i+1][j][1] = img[i+1][j+1][1]

	return img


def nnd_xtrans(img, x_offset, y_offset):
	""" Replaces channel information by taking the nearest neighbor's value """
	return img