```md
# Hand Tracker Application

A real-time hand tracking and gesture recognition application developed in Python using OpenCV, MediaPipe, and Tkinter.

The application provides real-time hand landmark detection and gesture analysis through computer vision techniques.

---

# System Requirements

## Required Software

Before running the application, ensure the following requirements are installed:

- Python 3.11.x (64-bit)
- Windows Operating System
- pip package manager

---

# Dependencies

This project uses the following Python libraries:

| Library | Purpose |
|---|---|
| MediaPipe | Hand detection and landmark tracking |
| OpenCV | Real-time camera processing |
| Pillow | Image processing support |
| Tkinter | Graphical User Interface |

---

# Important Environment Configuration

This project uses the MediaPipe Legacy Solutions API:

```

mp.solutions.hands

```

Newer MediaPipe versions may no longer support this API structure. Running the application with unsupported versions may cause the following error:

```

AttributeError: module 'mediapipe' has no attribute 'solutions'

```

To prevent compatibility issues, the project requires:

```

Python 3.11.x
MediaPipe 0.10.9

````

---

# Installation Guide

Follow each step carefully to configure the application.

---

# Step 1: Clone or Open the Project

Open the project folder using Command Prompt or Terminal.

Example:

```cmd
cd HandTracker
````

---

# Step 2: Create a Virtual Environment

Create a dedicated Python environment for the project.

```cmd
py -3.11 -m venv .venv
```

This creates an isolated environment where project dependencies can be installed safely.

---

# Step 3: Activate Virtual Environment

Activate the created environment.

```cmd
.venv\Scripts\activate
```

After successful activation, the terminal should display:

```
(.venv)
```

---

# Step 4: Confirm Python Version

Verify that the correct Python interpreter is being used.

```cmd
python --version
```

Required output:

```
Python 3.11.x
```

---

# Step 5: Install Project Dependencies

Install the required packages.

```cmd
pip install opencv-python pillow
```

Install the compatible MediaPipe version:

```cmd
pip install mediapipe==0.10.9
```

---

# Step 6: Verify Installed Packages

Check that MediaPipe is installed correctly.

```cmd
pip show mediapipe
```

Expected version:

```
Version: 0.10.9
```

---

# Running the Application

Execute the application from the project root directory.

```cmd
python main.py
```

The system will start the graphical interface and initialize the hand tracking module.

---

# Application Workflow

```
Application Start
        |
        v
Initialize Camera
        |
        v
Capture Video Frames
        |
        v
Process Frames Using OpenCV
        |
        v
Detect Hand Landmarks Using MediaPipe
        |
        v
Analyze Hand Gestures
        |
        v
Display Results Through Tkinter GUI
```

---

# Troubleshooting Guide

## Problem 1: MediaPipe Solutions API Error

Error:

```
AttributeError: module 'mediapipe' has no attribute 'solutions'
```

Cause:

The installed MediaPipe version is incompatible with the project requirements.

Solution:

Remove the current MediaPipe installation:

```cmd
pip uninstall mediapipe
```

Install the required version:

```cmd
pip install mediapipe==0.10.9
```

---

## Problem 2: Incorrect Python Version

Cause:

The application is running on Python versions not supported by the MediaPipe Legacy API.

Solution:

Check your Python version:

```cmd
python --version
```

Install and use Python 3.11.x.

---

## Problem 3: Virtual Environment Activation Failed

Error:

```
The system cannot find the path specified
```

Cause:

The `.venv` folder does not exist or the command is being executed outside the project directory.

Solution:

Recreate the environment:

```cmd
py -3.11 -m venv .venv
```

Activate again:

```cmd
.venv\Scripts\activate
```

---

# Project Structure

```
HandTracker/
│
├── main.py
├── .venv/
│
├── requirements.txt
│
├── assets/
│
└── README.md
```

---

# Development Environment

The project was tested using:

```
Operating System:
Windows

Python:
3.11.x (64-bit)

MediaPipe:
0.10.9

OpenCV:
Latest Compatible Version

GUI Framework:
Tkinter
```

---

# License

This project is intended for educational and development purposes.

```
```
