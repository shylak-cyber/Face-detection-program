# Face-detection-program
#It has some issue about detecting the objects because of the yolo modle , i think the model is not train well so ,but no problem it can detect  80+ object. so use the library 
It detect your face and object through model that is pre install in a module . it's a python program that is good to start as beginning.
This project performs real-time face detection and object detection using a webcam.
It combines:

Haar Cascade Classifier for face detection

YOLOv8 (You Only Look Once) for detecting multiple objects such as person, bottle, car, etc.

The program captures live video from the camera, detects faces and objects, and displays bounding boxes with labels and confidence scores.

🚀 Features

Real-time webcam detection

Face detection using OpenCV Haar Cascades

Object detection using YOLOv8 pretrained model

Displays object name and confidence

Lightweight YOLOv8n model (fast and efficient)

🛠️ Technologies Used

Python 3.x

OpenCV (cv2)

Ultralytics YOLOv8

Haar Cascade Classifier

📦 Requirements

Install the required libraries using pip:

pip install opencv-python
pip install ultralytics


Make sure you have:

A working webcam

Internet connection (first time YOLO model download)

📁 Files Used

yolov8n.pt → YOLOv8 pretrained model (automatically downloaded)

haarcascade_frontalface_default.xml → OpenCV face detection model

▶️ How to Run

Clone this repository or copy the code into a Python file (e.g., main.py)

Open terminal / command prompt

Run the program:

python main.py


Press ESC to exit the application

🧠 How It Works

Captures video frames from the webcam

Converts frame to grayscale for face detection

Detects faces using Haar Cascade

Detects objects using YOLOv8

Draws bounding boxes and labels on detected faces and objects

Displays the output in a window

📷 Output

Blue rectangle → Face detection

Green rectangle → Object detection

Label + confidence shown above detected objects

⚠️ Notes

YOLOv8 detects general objects, not faces (face detection is handled separately)

Performance depends on system hardware

For better speed, use a GPU if available

🔮 Future Improvements

Replace Haar Cascade with YOLO face detection

Add object counting

Save detection results to a file

Add voice feedback for detected objects

👨‍💻 Author

Lakshy Prajapat
B.Tech Computer Science Engineering
Python | Computer Vision | AI Enthusiast
