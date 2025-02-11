import cv2
import numpy as np

# Create two test images (image1 and image2)
image1 = np.zeros((300, 300, 3), dtype=np.uint8)
image1[:] = (230, 0, 0)  # Blue image 

image2 = np.zeros((300, 300, 3), dtype=np.uint8)
image2[:] = (0, 255, 0)  # Green image 

# Save the images for reference
cv2.imwrite("image1.jpg", image1)
cv2.imwrite("image2.jpg", image2)

# Display the original images
cv2.imshow("Original Image 1", image1)
cv2.waitKey(0)

# Brightness Adjustment
bright_img = cv2.add(image1, np.array([100.0])) 
cv2.imshow("Brightened Image", bright_img)
cv2.waitKey(0)

# Contrast Adjustment 
contrast_img = cv2.multiply(image1, np.array([0.5]))  
cv2.imshow("Lower Contrast Image", contrast_img)
cv2.waitKey(0)

cv2.imshow("Original Image 2", image2)
cv2.waitKey(0)

# Linear Blending 
alpha = float(input("Enter alpha (0-1) for blending: "))  # user input for blend ratio
blended_img = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)
cv2.imshow("Blended Image", blended_img)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()
