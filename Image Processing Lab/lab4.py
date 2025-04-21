import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load original image in grayscale
image = cv2.imread('m_pic.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found. Make sure 'my_pic.jpg' exists.")
    exit()

# 1. Negative Image
negative = 255 - image

# 2. Brightness Enhancement (add value to pixels)
brightness = cv2.convertScaleAbs(image, alpha=1, beta=50)  # beta adds brightness

# 3. Log Transformation
c = 255 / np.log(1 + np.max(image))  # scaling constant
log_trans = c * np.log(1 + image.astype(np.float32))
log_trans = np.array(log_trans, dtype=np.uint8)

# 4. Power-Law (Gamma) Transformation
gamma = 0.4  # Try 0.4 < γ < 1 for brightening, >1 for darkening
power_law = np.power(image / 255.0, gamma)
power_law = np.uint8(power_law * 255)

# 5. Contrast Enhancement (Histogram Equalization)
contrast = cv2.equalizeHist(image)

# Display all results using matplotlib
titles = ['Original', 'Negative', 'Brightness +50', 'Log Transform', 'Gamma = 0.4', 'Contrast Enhanced']
images = [image, negative, brightness, log_trans, power_law, contrast]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
