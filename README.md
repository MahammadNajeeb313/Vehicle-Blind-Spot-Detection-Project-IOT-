# Vehicle-Blind-Spot-Detection-Project-IOT-

Vehicle Blind Spot Detection using a Arduino

# Description

This a IoT based project used to detect a blind spots of a vehicles like Truck and Car using a Camera and it Sends an alert message to a driver, if any vehicles are detected in a blind spot using a buzzer.

# Development boards needed 

1.Arduino Uno
2.ESP32CAM
3.ESP8266 nodemcu
4.Buzzer
5.Jumper Wires

#  Step 1: Fix the Camera in the Blind Spot

Start by selecting a suitable camera for your project, such as the ESP32-CAM, which combines a microcontroller with a camera module. Mount the camera securely in the vehicle’s blind spot, ensuring it has a clear view of the area you wish to monitor.

#  Step 2: Draw the Region of Interest Using Python

Using Python, you can define a region of interest (ROI) where the camera will focus on detecting vehicles. You can use libraries like OpenCV to draw bounding boxes around the areas you want to monitor. This step 
is crucial as it helps your detection algorithm focus only on relevant parts of the image.

#  Step 3: Detect Vehicles Using YOLOv8

For vehicle detection within the defined ROI, you can utilize YOLOv8 (You Only Look Once), which is the fastest real-time object detection algorithm. You will need to install the necessary libraries and download a pre-trained YOLOv8 model. The following is an outline of how to implement it:
  # Install YOLOv8: Use pip to install necessary libraries.
  pip install ultralytics
  # Load and Run YOLOv8: python code
  from ultralytics import YOLO
  # Load model
  model = YOLO('yolov8n.pt')
  # Perform inference on the captured frame
  results = model(frame)

# Step 4: Alert System Using Arduino 

Finally, integrate an alert system using Arduino for notifying drivers when vehicles are detected in their blind spot. This can be done via serial communication between your Python script and Arduino.

# Arduino Setup:

Connect Arduino Uno to your ESP32 Cam.
Connect a Buzzer to your ESP8266 Nodemcu board.
Write Arduino Code to listen for serial messages:

____________________________________(REFER A CODES PROVIDED)_________________________________________________


By following these steps — installing a camera in the blind spot, detecting vehicles using YOLOv8, interacting with Python and integrating an alert system with Arduino — you can successfully create a functional Blind Spot Detection for vehicles. 

