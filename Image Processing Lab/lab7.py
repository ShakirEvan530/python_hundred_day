import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('my_pic.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: 'my_pic.jpg' not found.")
    exit()

# Define mask sizes
kernel_sizes = [3, 5, 7, 9]

# Display setup
plt.figure(figsize=(12, 10))
index = 1

for k in kernel_sizes:
    # --- Mean (Average) Filter ---
    mean_filtered = cv2.blur(image, (k, k))

    # --- Median Filter ---
    median_filtered = cv2.medianBlur(image, k)

    # Show Mean Filter result
    plt.subplot(len(kernel_sizes), 2, index)
    plt.imshow(mean_filtered, cmap='gray')
    plt.title(f'Mean Filter ({k}x{k})')
    plt.axis('off')
    index += 1

    # Show Median Filter result
    plt.subplot(len(kernel_sizes), 2, index)
    plt.imshow(median_filtered, cmap='gray')
    plt.title(f'Median Filter ({k}x{k})')
    plt.axis('off')
    index += 1

plt.tight_layout()
plt.show()
