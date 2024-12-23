# Import the dependencies
import cv2
import argparse
import sys

def main(path):

	# reading the image
	img = cv2.imread(path)

	# Make sure img is not empty
	if img is None:
	    print("Can't read the image file."+
	    "\nPlease make sure you are passing a valid path and it points to an image.")
	    sys.exit()

	img_sketch_bw, img_sketch_c = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

	# Fetch both the black and white pencil sketch and Colored Pencil Sketch

	# The smoothing filter replaces the value of a pixel by the weighted sum of its neighbors
	# The bigger the neighbourhood, the smoother the image becomes
	# The parameter signma_s(Sigma_Spatial) is used for controlling the size of the neighbourhood.
	# It's value are from 1-200

	# At times it is not possible to replace the color of a pixel by the weighted sum of its neighbors. 
	# Rather color value at a pixel is repaced by the average of pixels in the neighborhood which also have color similar to the pixel.
	# The parameter sigma_r(Sigma_Range) is used for controlling the averaging of dissimilar colors within the neighbourhood. 
	# It's value range from 0 to 1
	# A larger value of sigma_r results in large regions of constant color.

	# Shade Factor is used for scaling the output image intensity
	# It's value range from 0 to 1
	# A larger value of shade_factor results in a brighter image

	# Save the image in the desired path
	cv2.imwrite('assets/b&w_sketch.jpg', img_sketch_bw)
	cv2.imwrite('assets/color_sketch.jpg', img_sketch_c)
	
