# Hand Tracker Application

A real-time hand tracking and gesture recognition application developed using **Python**, **OpenCV**, **MediaPipe**, and **Tkinter**.

This application utilizes computer vision techniques to perform real-time hand landmark detection, gesture analysis, and visual feedback through a graphical user interface.

---

# System Requirements

## Required Software

Before running the application, ensure that the following requirements are installed:

- **Python 3.11.x (64-bit)**
- **Windows Operating System**
- **pip Package Manager**

---

# Dependencies

| Library | Purpose |
|---|---|
| MediaPipe | Hand detection and landmark tracking |
| OpenCV | Real-time camera processing |
| Pillow | Image processing support |
| Tkinter | Graphical User Interface |

---

# Important Compatibility Configuration

This project uses the MediaPipe Legacy Solutions API:

```python
mp.solutions.hands
```

Newer MediaPipe versions may no longer support this API structure.

If an unsupported version is installed, the following error may appear:

```
AttributeError: module 'mediapipe' has no attribute 'solutions'
```

Required versions:

```
Python:
3.11.x

MediaPipe:
0.10.9
```

---

# Installation Guide

Follow each step carefully to properly configure and run the application.

---

# **STEP 1: Open the Project Directory**

Navigate to the project folder using Command Prompt or Terminal.

Example:

```cmd
cd HandTracker
```

---

# **STEP 2: Create a Virtual Environment**

Create an isolated Python environment for the project.

```cmd
py -3.11 -m venv .venv
```

The virtual environment separates project dependencies from the system Python installation.

---

# **STEP 3: Activate the Virtual Environment**

Activate the created environment.

```cmd
.venv\Scripts\activate
```

Successful activation will display:

```
(.venv)
```

---

# **STEP 4: Verify Python Version**

Confirm that the correct Python version is being used.

```cmd
python --version
```

Required output:

```
Python 3.11.x
```

---

# **STEP 5: Install Required Dependencies**

Install the required Python libraries:

```cmd
pip install opencv-python pillow
```

Install the compatible MediaPipe version:

```cmd
pip install mediapipe==0.10.9
```

---

# **STEP 6: Verify Installed Packages**

Check if MediaPipe was installed correctly.

```cmd
pip show mediapipe
```

Expected output:

```
Version: 0.10.9
```

---

# **STEP 7: Run the Application**

Start the application from the project root directory.

```cmd
python main.py
```

The system will initialize the graphical interface and begin real-time hand tracking.

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

## MediaPipe Compatibility Error

Error:

```
AttributeError: module 'mediapipe' has no attribute 'solutions'
```

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

## Incorrect Python Version

Check the current Python version:

```cmd
python --version
```

Install Python 3.11.x if another version is being used.

---

## Virtual Environment Error

Error:

```
The system cannot find the path specified
```

Solution:

Recreate the virtual environment:

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
├── requirements.txt
├── .venv/
│
├── assets/
│
└── README.md
```

---

# Development Environment

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

This project is created for **educational and academic purposes**.

The source code is provided as a learning resource for studying computer vision, hand tracking technology, and graphical user interface development.

Users may:

- Study and understand the implementation
- Modify the source code for educational purposes
- Use the project as a reference for academic learning

Commercial distribution or unauthorized use of this project is not permitted without approval from the original developer.

By using this project, users acknowledge that it is intended as an educational resource and should be used responsibly.
