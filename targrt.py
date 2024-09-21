import cv2
import numpy as np

# Load the main image and the template (target image)
main_image = cv2.imread('/home/tacodi/python opencv/whackabot/mainimage.png')
template = cv2.imread('/home/tacodi/python opencv/whackabot/noiseimg.png')

# Convert both images to grayscale
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Get the width and height of the template
w, h = template_gray.shape[::-1]

# Perform template matching
result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Set a threshold to filter out low-matching regions
threshold = 0.8
loc = np.where(result >= threshold)

# Draw rectangles on all the matched regions
for pt in zip(*loc[::-1]):
    cv2.rectangle(main_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# Show the result
cv2.imshow('Detected Image', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
