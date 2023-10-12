# import the necessary packages

import cv2
import numpy as np
import matplotlib.pyplot as plt

# load the image and convert it to grayscale 
img = cv2.imread('Z.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#-------------------------Canny-------------------------#

# Canny edge detection
img_canny = cv2.Canny(img,100,200)
"""
- .canny() means that it will implement the Canny edge detection algorithm.
- The first argument is our input image.
- The second and third arguments are our minVal and maxVal respectively.
    - 100 and 200 are normally good enough threshold values. 
        - pixels with values higher than threshold are strong edge pixels
        - pixels with values lower than threshold are non edge pixels
        - pixels with values in between threshold are weak potential edge pixels
"""

#-------------------------Sobel and Prewitt-------------------------#

# Sobel edge detection
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

# Explanation of Sobel function parameters
"""
.Sobel() function is used to detect the edges.
img_gaussian is the image on which gaussian filter is applied to reduce the noise for better edge detection performance.
cv2.CV_8U is the data type of the output image that is 8 bit unsigned integer.
1 and 0 are the order of the derivatives in x and y direction respectively.
    - 1 mean that the derivative of the image in x direction is to be taken.
    - 0 mean that the derivative of the image in y direction is to be taken.
ksize=5 is the size of the kernel used for the operation.
"""

#-------------------------Prewitt-------------------------#

#prewitt edge detection
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

# Explanation of prewitt function parameters
"""
- filter2D is the function to convolve a kernel with an image it apply prewitt algorithm.
- The first argument is the source image. source image is gaussian image to remove if any noise in image.
- [-1] means destination image will have depth same as input image depth.
- kernel is the matrix with which convolution is to be done. 
"""

#-------------------------Display-------------------------#

# Display the images using matplotlib
plt.figure(figsize=(10, 7))
plt.subplot(3, 3, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap='gray'), plt.title('Original Image')
plt.subplot(3, 3, 2), plt.imshow(img_canny, cmap='gray'), plt.title('Canny')
plt.subplot(3, 3, 3), plt.imshow(img_sobelx, cmap='gray'), plt.title('Sobel X')
plt.subplot(3, 3, 4), plt.imshow(img_sobely, cmap='gray'), plt.title('Sobel Y')
plt.subplot(3, 3, 5), plt.imshow(img_sobel, cmap='gray'), plt.title('Sobel')
plt.subplot(3, 3, 6), plt.imshow(img_prewittx, cmap='gray'), plt.title('Prewitt X')
plt.subplot(3, 3, 7), plt.imshow(img_prewitty, cmap='gray'), plt.title('Prewitt Y')
plt.subplot(3, 3, 8), plt.imshow(img_prewittx + img_prewitty, cmap='gray'), plt.title('Prewitt')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
