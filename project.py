import cv2
from ultralytics import YOLO
import requests

# URL of the ESP32-CAM MJPEG stream
url = "http://IP_of_esp32cam:81/stream"  # Replace with your ESP32-CAM IP address

# API endpoint URL to trigger (replace with your endpoint)
api_url = "http://IP_of_esp8266_nodemcu/beep"

# Load the YOLOv8 model (pre-trained weights)
model = YOLO("yolov8n.pt")  # Use "yolov8n.pt" for the nano model (you can choose others like yolov8s.pt, yolov8m.pt, etc.)

# Open the MJPEG stream using OpenCV VideoCapture
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    
    if ret:
        # Perform object detection on the current frame using YOLOv8
        results = model(frame)  # This gives us the predictions

        # Check if "car" or "truck" is detected in the frame
        for detection in results[0].boxes:
            cls_name = model.names[int(detection.cls)]  # Get the class name of the detected object
            if cls_name in ["car", "truck"]:
                print(f"Detected: {cls_name}. Triggering API call...")
                requests.get(api_url)
                try:
                    response = requests.get(api_url)  # Trigger the API endpoint
                    if response.status_code == 200:
                        print("API call successful!")
                    else:
                        print(f"API call failed with status code: {response.status_code}")
                except Exception as e:
                    print(f"Error calling API: {e}")

        # Visualize the results on the frame (draw bounding boxes)
        frame = results[0].plot()  # This draws boxes, labels, etc., directly on the frame

        # Show the frame with detections
        cv2.imshow("ESP32-CAM Stream with YOLOv8", frame)

        # Wait for a key press to close the window (e.g., 'q' key)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to read frame")

# Release resources
cap.release()
cv2.destroyAllWindows()
