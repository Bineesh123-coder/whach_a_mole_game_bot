import cv2

template = cv2.imread('/home/tacodi/python opencv/sample.jpg')
if template is not None:
    cv2.imshow("Image Window", template)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found.")

