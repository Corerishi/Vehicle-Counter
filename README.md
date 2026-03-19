# 🚗 Vehicle Counter

> **Real-time vehicle detection and counting from video footage** using OpenCV background subtraction and contour-based centroid tracking.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Arrays-013243?style=flat&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)

---

## 🧠 What is this?

**Vehicle Counter** is a Python computer vision script that processes a traffic video, detects moving vehicles frame-by-frame, and counts how many cross a configurable detection line.

It uses **MOG (Mixture of Gaussians) background subtraction** to isolate moving objects, then applies morphological operations and contour detection to identify and track vehicles — no deep learning required.

---

## ✨ Features

- 🎥 **Video-based detection** — works on any MP4 traffic footage
- 🟩 **Bounding box rendering** — draws green rectangles around detected vehicles
- 📍 **Centroid tracking** — tracks the center point of each detected vehicle
- 〰️ **Configurable count line** — horizontal line trigger with pixel offset tolerance
- 🔢 **Live counter overlay** — vehicle count displayed directly on the video frame
- ⚙️ **Tunable parameters** — min bounding box size, line position, and offset all configurable

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Computer Vision** | OpenCV (`cv2`) |
| **Background Subtraction** | MOG — `cv2.bgsegm.createBackgroundSubtractorMOG()` |
| **Morphological Processing** | Dilation + `MORPH_CLOSE` (ellipse kernel) |
| **Contour Detection** | `cv2.findContours` |
| **Numerical Operations** | NumPy |

---

## 🔬 How It Works

```
Read video frame-by-frame
        │
        ▼
  Convert to Grayscale → Gaussian Blur
        │
        ▼
  MOG Background Subtraction
  (isolates moving foreground objects)
        │
        ▼
  Morphological Operations
  (dilation + MORPH_CLOSE to fill gaps)
        │
        ▼
  Find Contours
  (filter by min width/height to remove noise)
        │
        ▼
  Compute Centroid of each valid contour
  + Draw bounding box
        │
        ▼
  Check if centroid crosses count line
  (within ±OFFSET pixels)
        │
        ▼
  Increment counter + update display
```

---

## ⚙️ Configuration

All key parameters are at the top of `main.py` — no need to dig into the logic:

```python
VIDEO_PATH   = 'video.mp4'  # Path to your traffic video
MIN_WIDTH    = 80            # Min bounding box width (filters out small noise)
MIN_HEIGHT   = 80            # Min bounding box height
COUNT_LINE_Y = 550           # Y-coordinate of the counting line
OFFSET       = 6             # Pixel tolerance around the line (±6px)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- OpenCV contrib (required for MOG background subtractor)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Corerishi/Vehicle-Counter.git
cd Vehicle-Counter

# 2. Install dependencies
pip install opencv-contrib-python numpy
```

> ⚠️ Make sure to install `opencv-contrib-python` (not just `opencv-python`) — the MOG background subtractor is part of the contrib modules.

### Run

```bash
# Place your traffic video in the project folder as video.mp4, then:
python main.py

# Press 'q' to quit at any time
```

---

## 📁 Project Structure

```
Vehicle-Counter/
├── main.py        # Main detection + counting script
├── video.mp4      # Your input traffic video (not included)
└── README.md
```

---

## 📚 Concepts Demonstrated

- **Background subtraction** — MOG algorithm to separate moving objects from static background
- **Morphological image processing** — dilation and closing to improve contour quality
- **Contour detection & filtering** — extracting and validating vehicle shapes
- **Centroid-based object tracking** — tracking movement across frames without deep learning
- **Real-time video processing** — frame-by-frame OpenCV pipeline

---

## 👨‍💻 Author

**Rishi Raj**  
MCA — CHRIST (Deemed to be University)  
[LinkedIn](https://linkedin.com/in/rishi-raj-9110a824a) · [GitHub](https://github.com/Corerishi)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
