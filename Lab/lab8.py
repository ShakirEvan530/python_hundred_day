import cv2
import matplotlib.pyplot as plt

# Load grayscale image
image = cv2.imread('my_pic.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: 'my_pic.jpg' not found.")
    exit()

# Apply Histogram Equalization
equalized = cv2.equalizeHist(image)

# Show Original and Equalized images with histograms
plt.figure(figsize=(10, 6))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Equalized image
plt.subplot(2, 2, 2)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')

# Histogram of original
plt.subplot(2, 2, 3)
plt.hist(image.ravel(), 256, [0, 256])
plt.title("Original Histogram")

# Histogram of equalized
plt.subplot(2, 2, 4)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()
