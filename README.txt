# Hand Tracker Application

A real-time hand tracking and gesture analysis application developed in Python utilizing OpenCV, MediaPipe, and Tkinter.

---

## Technical Architecture & Dependencies

This project relies on the **MediaPipe Legacy Solutions API** (`mp.solutions.hands`). Because Google has deprecated and removed this API interface from modern versions, strict version pinning is required. 

Executing this application with unsupported environments (e.g., Python 3.12+ or MediaPipe 0.10.15+) will trigger runtime exceptions, specifically: `AttributeError: module 'mediapipe' has no attribute 'solutions'`.

### Validated Environment Specification
* **Runtime Environment:** Python 3.11.x (64-bit)
* **Core Libraries:** 
  * `mediapipe==0.10.9` (Strictly enforced)
  * `opencv-python`
  * `pillow`

---

## Deployment and Setup

Follow these steps to isolate your dependencies and deploy the project locally on Windows environments.

### 1. Initialize the Virtual Environment
Generate an isolated virtual environment explicitly targeted to a Python 3.11 interpreter using the Python Launcher:
```cmd
py -3.11 -m venv .venv
```

### 2. Activate the Environment
Isolate your terminal session context to the newly created environment:
```cmd
.venv\Scripts\activate
```
*Note: Your terminal prompt prefix will change to `(.venv)` upon successful activation.*

### 3. Verify Environment Integrity
Confirm that the runtime environment is correctly mapped to the specified Python version:
```cmd
python --version
```
*Expected Output:* `Python 3.11.x`

### 4. Install Component Dependencies
Install the standard dependencies and force-provision the precise version of the MediaPipe wheel asset:
```cmd
pip install opencv-python pillow
pip install --force-reinstall mediapipe==0.10.9
```

---

## Execution

Launch the main application interface entry point from the project root folder:
```cmd
python main.py
```

---

## Troubleshooting

### Runtime Exception: `AttributeError: module 'mediapipe' has no attribute 'solutions'`
* **Root Cause:** The active environment is utilizing an unaligned Python version (such as Python 3.14) or has pulled a newer MediaPipe distribution downstream.
* **Resolution:** Verify your version constraint profiles via `pip show mediapipe`. Rectify mismatches by executing:
  ```cmd
  pip install --force-reinstall mediapipe==0.10.9
  ```

### Activation Fault: `The system cannot find the path specified`
* **Root Cause:** The targeted activation script destination does not exist within the active working directory structure.
* **Resolution:** Ensure step 1 executed flawlessly without syntax exceptions and that the `.venv` directory tree physically resides inside your local repository workspace root.
