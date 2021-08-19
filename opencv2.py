# simple program to read and show an image


import cv2



img = cv2.imread("a.jpeg")
gray = cv2.imread('a.jpeg',cv2.IMREAD_GRAYSCALE)
gray1 = cv2.imread('a.jpeg',cv2.IMREAD_REDUCED_GRAYSCALE_2)

cv2.imshow('ziaul kadri',img)
cv2.imshow('gray ziaul kadri',gray)
cv2.imshow('gray ziaul kadri',gray1)




cv2.waitKey(0)
cv2.destroyAllWindows()