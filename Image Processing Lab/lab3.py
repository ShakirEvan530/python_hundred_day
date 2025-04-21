import cv2
import numpy as np

# Load the image in grayscale
gray_image = cv2.imread('m_pic.jpg', cv2.IMREAD_GRAYSCALE)

# Convert grayscale to RGB
rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)

# Show the RGB image (optional GUI)
cv2.imshow('RGB Image', rgb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the RGB image matrix
print("Image Matrix:")
print(rgb_image)

# Rgb image matrix of this image
# [[[ 59  59  59]
#   [ 56  56  56]
#   [ 50  50  50]
#   ...
#   [ 71  71  71]
#   [ 54  54  54]
#   [ 53  53  53]]
#
#  [[ 52  52  52]
#   [ 49  49  49]
#   [ 56  56  56]
#   ...
#   [ 96  96  96]
#   [ 84  84  84]
#   [ 89  89  89]]
#
#  [[ 43  43  43]
#   [ 45  45  45]
#   [ 44  44  44]
#   ...
#   [ 81  81  81]
#   [ 71  71  71]
#   [ 81  81  81]]
#
#  ...
#
#  [[119 119 119]
#   [121 121 121]
#   [112 112 112]
#   ...
#   [119 119 119]
#   [107 107 107]
#   [122 122 122]]
#
#  [[133 133 133]
#   [135 135 135]
#   [134 134 134]
#   ...
#   [ 90  90  90]
#   [ 95  95  95]
#   [ 93  93  93]]
#
#  [[107 107 107]
#   [104 104 104]
#   [114 114 114]
#   ...
#   [106 106 106]
#   [104 104 104]
#   [ 98  98  98]]]
