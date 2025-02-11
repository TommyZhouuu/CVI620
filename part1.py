import cv2

# Open webcam
cap = cv2.VideoCapture(0)  # 0 represents the default webcam
count = 1  # Counter for snapshot filenames

while True:
    ret, frame = cap.read()  
    if not ret:
        break

    cv2.imshow("Photo Booth", frame)  

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  
        filename = f"part{count}.jpg"
        cv2.imwrite(filename, frame)  # Save image
        print(f"Saved: {filename}")
        count += 1
    elif key == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
