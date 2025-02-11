import cv2
import numpy as np

# Create a blank image (Black background)
img = np.zeros((400, 600, 3), dtype=np.uint8)

# 1.1 Draw Green Rectangle (Thickness = 4) 
cv2.rectangle(img, (100, 100), (500, 300), (0, 255, 0), 4)  # Green Rectangle
cv2.imshow("Rectangle (Thickness 4)", img)
cv2.waitKey(0)

# 1.2 Change Thickness to -1 
cv2.rectangle(img, (100, 100), (500, 300), (0, 255, 0), -1)  
cv2.imshow("Rectangle (Filled)", img)
cv2.waitKey(0)

# 1.3 Add Text on the Rectangle 
cv2.putText(img, "Xuesong Zhou", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow("Rectangle with Text", img)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()
