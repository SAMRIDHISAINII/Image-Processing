import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread("input.jpg")
cv2_imshow(img)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2_imshow( gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
