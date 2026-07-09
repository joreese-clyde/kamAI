```md
# Hand Tracker Application

A real-time hand tracking and gesture analysis application developed using Python, OpenCV, MediaPipe, and Tkinter.

---

# Technical Architecture and Dependencies

This project utilizes the MediaPipe Legacy Solutions API (`mp.solutions.hands`) for real-time hand detection and gesture analysis.

Due to the deprecation and removal of this API interface in newer MediaPipe versions, this application requires a specific environment configuration to function correctly.

Using unsupported environments, such as Python 3.12+ or MediaPipe versions newer than `0.10.9`, may result in runtime errors:

```

AttributeError: module 'mediapipe' has no attribute 'solutions'

````

---

# Validated Environment Specification

**Runtime Environment**

- Python Version: Python 3.11.x (64-bit)

**Required Dependencies**

- mediapipe==0.10.9
- opencv-python
- pillow

---

# Installation and Setup

Follow the steps below to properly configure and run the application.

---

# Step 1: Create a Virtual Environment

Create an isolated Python virtual environment using Python 3.11.

```cmd
py -3.11 -m venv .venv
````

---

# Step 2: Activate the Virtual Environment

Activate the created virtual environment before installing dependencies.

```cmd
.venv\Scripts\activate
```

Successful activation will display:

```
(.venv)
```

at the beginning of your terminal prompt.

---

# Step 3: Verify Python Version

Confirm that the active environment is using the required Python version.

```cmd
python --version
```

Expected output:

```
Python 3.11.x
```

---

# Step 4: Install Required Dependencies

Install the required libraries and enforce the compatible MediaPipe version.

```cmd
pip install opencv-python pillow
```

Install the required MediaPipe version:

```cmd
pip install --force-reinstall mediapipe==0.10.9
```

---

# Running the Application

Navigate to the project root directory and execute the main application file.

```cmd
python main.py
```

The Hand Tracker Application interface will launch successfully if the environment is configured correctly.

---

# Troubleshooting

## Error: AttributeError: module 'mediapipe' has no attribute 'solutions'

### Cause

The installed MediaPipe version is incompatible with the Legacy Solutions API, or the project is running on an unsupported Python version.

### Solution

Check the installed MediaPipe version:

```cmd
pip show mediapipe
```

Reinstall the required version:

```cmd
pip install --force-reinstall mediapipe==0.10.9
```

Verify that Python is running on version 3.11.x.

---

## Error: The system cannot find the path specified

### Cause

The virtual environment activation script cannot be located because the `.venv` directory was not created correctly or the terminal is not inside the project directory.

### Solution

1. Confirm that the `.venv` folder exists inside the project directory.

2. Recreate the virtual environment:

```cmd
py -3.11 -m venv .venv
```

3. Activate the environment again:

```cmd
.venv\Scripts\activate
```

---

# Project Execution Flow

```
Create Virtual Environment
          |
          v
Activate Environment
          |
          v
Verify Python Version
          |
          v
Install Dependencies
          |
          v
Run main.py
          |
          v
Hand Tracking Application Starts
```

```
```
