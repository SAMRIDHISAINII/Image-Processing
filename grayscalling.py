import cv2

# Load the color image
image = cv2.imread("input.jpg")

# Convert the image to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2_imshow(gray_image)
cv2.waitKey(0)
