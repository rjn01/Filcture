# Import the dependencies
import cv2
import argparse
import sys

# construct the argument parse and parse the arguments


# reading the image
img = cv2.imread("/home/rjn/Pictures/My Pictures/rajan.jpeg")

# Make sure img is not empty
if img is None:
    print("Can't read the image file."+
    "\nPlease make sure you are passing a valid path and it points to an image.")
    sys.exit()

oil_painting_img = cv2.xphoto.oilPainting(img,7,1)

#create Window to display images
cv2.imshow('Oil Painting', oil_painting_img)

# Input keypress
k = cv2.waitKey(0)
# If Esc key is pressed
if k == 27 or k == ord('q'):
    # Save the image in the desired path
    cv2.imwrite('assets/oil_painting.jpg',oil_painting_img)
    #close all the opened windows
    cv2.destroyAllWindows()

