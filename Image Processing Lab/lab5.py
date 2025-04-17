import cv2
import numpy as np
import math

# Functions to calculate MSE and PSNR
def calculate_mse(original, distorted):
    return np.mean((original - distorted) ** 2)

def calculate_psnr(original, distorted):
    mse = calculate_mse(original, distorted)
    if mse == 0:
        return float('inf')  # Perfect match
    max_pixel = 255.0
    return 20 * math.log10(max_pixel / math.sqrt(mse))

# Load the original image
original = cv2.imread('my_pic.jpg', cv2.IMREAD_GRAYSCALE)
if original is None:
    print("Error: 'my_pic.jpg' not found.")
    exit()

# Load distorted images and resize to match original
distorted_images = {
    'Blurred': cv2.imread('blurred.jpg', cv2.IMREAD_GRAYSCALE),
    'Noisy': cv2.imread('noisy.jpg', cv2.IMREAD_GRAYSCALE),
    'Compressed': cv2.imread('compressed.jpg', cv2.IMREAD_GRAYSCALE)
}

# Calculate and display MSE and PSNR
for name, img in distorted_images.items():
    if img is None:
        print(f"Error: '{name}' image not found.")
        continue

    # Resize distorted image to match original
    img_resized = cv2.resize(img, (original.shape[1], original.shape[0]))

    mse = calculate_mse(original, img_resized)
    psnr = calculate_psnr(original, img_resized)

    print(f"{name} Image:")
    print(f"  ➤ MSE  = {mse:.2f}")
    print(f"  ➤ PSNR = {psnr:.2f} dB\n")
