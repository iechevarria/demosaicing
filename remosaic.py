""" Generate synthetic data by eliminating color channel information """

from PIL import Image
import numpy as np


def to_bayer(img, x_offset = 0, y_offset = 0):
	""" Eliminates channel information to simulate a Bayer CFA 
		@param 3D numpy array img
		@param int x_offset
		@param int y_offset
		@return img """

	for i in range(int(img.shape[0])):
		y = i + y_offset
		for j in range(int(img.shape[1])):
			x = j + x_offset
			dy = y % 2
			dx = x % 2
			# blue row elimination
			if dy == 0:
				# delete blue, red
				if dx == 0:
					img[i][j][2] = img[i][j][0] = 0
				# delete green, red
				else:
					img[i][j][1] = img[i][j][0] = 0

			# red row elimination
			else:
				# delete green, blue
				if dx == 0:
					img[i][j][1] = img[i][j][2] = 0
				# delete red, blue
				else:
					img[i][j][0] = img[i][j][2] = 0

	return img


def to_xtrans(img, x_offset = 0, y_offset = 0):
	""" Eliminates channel information to simulate an X-Trans CFA 
		@param 3D numpy array img
		@param int x_offset
		@param int y_offset 
		@return img """
		
	for i in range(int(img.shape[0])):
		y = i + y_offset
		for j in range(int(img.shape[1])):
			x = j + x_offset
			dy = y % 6
			dx = x % 6
			# row 0 and 2 elminiation
			if dy in [0,2]:
				# blue: delete red, green
				if dx == 1:
					img[i][j][0] = img[i][j][1] = 0
				# red: delete blue, green
				elif dx == 4: 
					img[i][j][2] = img[i][j][1] = 0
				# green: delete red, blue
				else:
					img[i][j][0] = img[i][j][2] = 0

			# row 1 elimination
			elif dy == 1:
				# blue: delete red, green
				if dx in [3,5]:
					img[i][j][0] = img[i][j][1] = 0
				# green: delete red, blue
				elif dx in [1,4]:
					img[i][j][0] = img[i][j][2] = 0
				# red: delete blue, green
				else:
					img[i][j][2] = img[i][j][1] = 0

			# row 3 and 5 elimination
			elif dy in [3,5]:
				# blue: delete red, green
				if dx == 4: 
					img[i][j][0] = img[i][j][1] = 0
				# red: delete blue, green
				elif dx == 1:
					img[i][j][2] = img[i][j][1] = 0
				# green: delete red, blue
				else: 
					img[i][j][0] = img[i][j][2] = 0

			# row 4 elimination
			else:
				# blue: delete red, green
				if dx in [0,2]:
					img[i][j][0] = img[i][j][1] = 0
				# green: delete red, blue
				elif dx in [1,4]:
					img[i][j][0] = img[i][j][2] = 0
				# red: delete blue, green
				else:
					img[i][j][2] = img[i][j][1] = 0
				
	return img


def main():
	print("Basic Pattern Test")
	img = np.zeros((10,10,3), np.uint8)
	img[0:100,0:100,0:3] = 255
	out1 = Image.fromarray(img, 'RGB')
	out1.save("out1.png")
	bayer = to_bayer(img)
	out2 = Image.fromarray(bayer, 'RGB')
	out2.save("out2.png")
	img[0:100,0:100,0:3] = 255
	xtrans = to_xtrans(img)
	out3 = Image.fromarray(xtrans, 'RGB')
	out3.save("out3.png")


if __name__ == '__main__':
	main()