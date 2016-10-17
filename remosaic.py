from PIL import Image
import numpy as np


def toBayer(img, x_offset = 0, y_offset = 0):
	""" Eliminates channel information to simulate a Bayer CFA 
		@param 3d numpy array img
		@param int x_offset
		@param int y_offset
		@return img """

	for y in range(int(img.shape[0])):
		for x in range(int(img.shape[1])):
			
			# blue row elimination
			if (y + y_offset) % 2 == 0:

				# delete blue, red
				if (x + x_offset) % 2 == 0:
					img[y][x][2] = img[y][x][0] = 0
				# delete green, red
				else:
					img[y][x][1] = img[y][x][0] = 0

			# red row elimination
			else:

				# delete green, blue
				if (x + x_offset) % 2 == 0:
					img[y][x][1] = img[y][x][2] = 0
				# delete red, blue
				else:
					img[y][x][0] = img[y][x][2] = 0

	return img


def toXtrans(img, x_offset = 0, y_offset = 0):
	""" Eliminates channel information to simulate an X-Trans CFA 
		@TODO implement channel removal"""
		
	for y in range(int(img.shape[1])):
		for x in range(int(img.shape[2])):

			# row 0 and 2 elminiation
			if (y + y_offset) % 6 == 0 or (y + y_offset) % 6 == 2:
				 # delete red, green

				 # delete blue, green

				 # delete red, blue

			# row 1 elimination
			elif (y + y_offset) % 6 == 1:
				continue
			# row 3 and 5 elimination
			elif (y + y_offset) % 6 == 3 or (y + y_offset) % 6 == 5:
				continue
			# row 5 elimnination
			else:
				continue


def main():
	print("Basic Pattern Test")
	img = np.zeros((100,100,3), np.uint8)
	img[0:100,0:100,0:3] = 255
	out1 = Image.fromarray(img, 'RGB')
	out1.show()
	img = toBayer(img)
	out2 = Image.fromarray(img, 'RGB')
	out2.show()


if __name__ == '__main__':
	main()