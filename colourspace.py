import cv2 as cv

image = cv.imread('images/input.jpg')
cv.imshow('original',image)
cv.waitKey()

# BGR value of each pixel
B,G,R = image[10,50]
print(B,G,R)

#after coverting it into grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
print(gray_img[10, 50]) 

gray_img[0, 0] 

# HSV value
hsv_image = cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow('Saturation channel', hsv_image[:, :, 1])
cv.waitKey()

# Manipulate colors
B,G,R = cv.split(image)
cv.imshow('red only',R)
cv.waitKey()

merged = cv.merge([B,G,R+100])
cv.imshow('merged',merged)
cv.waitKey()

cv.destroyAllWindows()
