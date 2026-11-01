# Develop a Python program using NumPy to simulate basic image processing operations 
# by representing an image as a matrix of pixel values. The program should perform 
# operations such as reshaping the image matrix, slicing specific regions, applying 
# brightness adjustments using broadcasting, and performing matrix multiplication for 
# transformation effects. 


import numpy as np

# Create an image matrix (4x4)
image = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Image:")
print(image)

# 1. Reshaping the image
reshaped = image.reshape(2, 8)
print("\nReshaped Image (2x8):")
print(reshaped)

# 2. Slicing a specific region
region = image[0:2, 0:2]
print("\nSelected Image Region:")
print(region)

# 3. Brightness adjustment using broadcasting
bright_image = image + 50
bright_image = np.clip(bright_image, 0, 255)
print("\nImage After Brightness Adjustment:")
print(bright_image)

# 4. Matrix multiplication for transformation
transform = np.array([
    [1, 0],
    [0, 1]
])

small_image = image[0:2, 0:2]
transformed = np.dot(small_image, transform)

print("\nTransformed Image:")
print(transformed)
