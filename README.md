# PPE Kit Detection

The project focuses on developing a system to enhance safety in manufacturing environments by automatically detecting Personal Protective Equipment (PPE) on workers.
The system is designed to detect humans in restricted areas (No-Human Zones) and identify whether required PPE kits, such as helmets, radium jackets, boots, and goggles, are present on workers. It will also include face recognition functionality to verify worker identities.
Leveraging deep learning and object detection technologies, this system aims to improve compliance with safety protocols and reduce accidents in industrial settings.

## Features

- **Real-Time Detection:** Supports detection on live video streams.
- **Detection of PPE Items:** Identifies common PPE items such as helmets, gloves, safety vests, goggles, and masks.
- **Bounding Boxes and Labels:** Outputs results with bounding boxes and labels for each detected PPE item.
- **Visualization and Logging:** Includes capabilities for visualizing detections and logging results.

## Installation

### Prerequisites

Ensure all necessary dependencies are installed. Use the `requirements.txt` file for easy setup.

```bash
pip install -r requirements.txt
```

### Setup Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vishnuaku/PPE-Kit-Detection.git
   cd PPE-Kit-Detection
   ```

2. **Download Model Weights:**

   If pre-trained model weights are required, download them and place them in the `models` directory.

## Usage

### Video Detection

To perform detection on a specific video, update the `cap` variable in the `detect.py` script as follows:

```python
cap = cv2.VideoCapture("../Videos/ppe 1.1.mp4")  # For Video
```

### Real-Time Detection

To use the webcam for real-time detection, uncomment the following lines in the `detect.py` script:

```python
# cap = cv2.VideoCapture(0)  # For Webcam
# cap.set(3, 1280)
# cap.set(4, 720)
```

### Output

- **Visualization:** Detected items will be displayed with bounding boxes and labels on the screen.
- **Saving Results:** The results can be saved in the `output` directory.
