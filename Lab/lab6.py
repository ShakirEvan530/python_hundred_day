import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('my_pic.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found.")
    exit()

# Mask sizes to test
kernel_sizes = [3, 5, 7, 9]

# Plotting setup
plt.figure(figsize=(12, 8))
index = 1

for k in kernel_sizes:
    # --- Average (Mean) Filter ---
    avg_blur = cv2.blur(image, (k, k))

    # --- Weighted (Gaussian) Filter ---
    gauss_blur = cv2.GaussianBlur(image, (k, k), 0)

    # Show Average Filter result
    plt.subplot(len(kernel_sizes), 2, index)
    plt.imshow(avg_blur, cmap='gray')
    plt.title(f'Average Filter ({k}x{k})')
    plt.axis('off')
    index += 1

    # Show Weighted Filter result
    plt.subplot(len(kernel_sizes), 2, index)
    plt.imshow(gauss_blur, cmap='gray')
    plt.title(f'Gaussian Filter ({k}x{k})')
    plt.axis('off')
    index += 1

plt.tight_layout()
plt.show()
