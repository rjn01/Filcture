# Import the dependencies
import cv2


def main(path):
	# reading the image
	img = cv2.imread("/home/rjn/Pictures/My Pictures/rajan.jpeg")

	water_color_img  = cv2.stylization(img, sigma_s = 60,sigma_r = 0.6)
	# The smoothing filter replaces the value of a pixel by the weighted sum of its neighbors
	# The bigger the neighbourhood, the smoother the image becomes
	# The parameter signma_s(Sigma_Spatial) is used for controlling the size of the neighbourhood.
	# It's value are from 1-200

	# At times it is not possible to replace the color of a pixel by the weighted sum of its neighbors.
	# Rather color value at a pixel is repaced by the average of pixels in the neighborhood which also have color similar to the pixel.
	# The parameter sigma_r(Sigma_Range) is used for controlling the averaging of dissimilar colors within the neighbourhood.
	# It's value range from 0 to 1
	# A larger value of sigma_r results in large regions of constant color.

	
	# Save the image in the desired path
	cv2.imwrite('assets/water_coloring.jpg', water_color_img)
	
