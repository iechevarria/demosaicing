from demosaic import remosaic
from demosaic import nearest_neighbor

def main():
	img = Image.open("data/sample.jpg")
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