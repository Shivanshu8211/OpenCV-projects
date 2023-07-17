#frame tracking
import cv2

# Initialize video capture from webcam or video file
cap = cv2.VideoCapture(0)  # Change to 0 if using webcam or provide the path to a video file

# Read the first frame
ret, frame = cap.read()
prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Define the threshold for detecting motion
threshold = 30

while True:
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the current frame and the previous frame
    frame_diff = cv2.absdiff(current_frame, prev_frame)

    # Apply thresholding to get the binary image
    _, thresholded = cv2.threshold(frame_diff, threshold, 255, cv2.THRESH_BINARY)

    # Find contours of moving objects
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding rectangles around the moving objects
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Adjust the minimum contour area as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Object Tracking', frame)

    # Update the previous frame
    prev_frame = current_frame.copy()

    # Exit the program if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
