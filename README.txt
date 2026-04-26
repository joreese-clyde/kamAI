# 🖐️ Hand Tracking — Filipino Number Recognition

This is a simple computer vision project that detects hand gestures in real time using **MediaPipe** and **OpenCV**, then translates finger positions into Filipino number words.

| Fingers Up                       | Meaning |
| -------------------------------- | ------- |
| ✊ none                           | Wala    |
| ☝️ index                         | Isa     |
| ✌️ index + middle                | Dalawa  |
| 🤟 index + middle + ring         | Tatlo   |
| 🖖 index + middle + ring + pinky | Apat    |
| 🖐️ all fingers                  | Lima    |

---

## 📁 Project Overview

The project is split into small parts so it’s easier to understand:

* **hand_tracker/** → main logic (detection, gesture reading, drawing)
* **main.py** → runs the program
* **tests/** → simple tests for gesture logic
* **config.py** → settings like thresholds and tuning values

---

## 🚀 How to Run

### 1. Get the project

```bash
https://github.com/joreese-clyde/handtracker.git
cd handtracker
```

### 2. Setup environment

```bash
python -m venv .venv
```

Activate it:

* Windows:

```bash
.venv\Scripts\activate
```

* Mac/Linux:

```bash
source .venv/bin/activate
```

### 3. Install needed libraries

```bash
pip install -r requirements.txt
```

### 4. Download the hand model

```bash
curl -o hand_landmarker.task "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
```

### 5. Run the app

```bash
python main.py
```

Press **ESC** to stop.

---

##  Optional Controls

You can change how it runs:

```bash
python main.py --camera 0 --num-hands 2 --no-fps --no-skeleton
```

* `--camera` → choose webcam
* `--num-hands` → how many hands to detect
* `--no-fps` → hide FPS display
* `--no-skeleton` → hide hand lines

---

##  Testing

If you want to check the gesture logic:

```bash
pytest tests/ -v
```

---

##  Idea Behind It

The project works by:

1. Detecting hand landmarks using MediaPipe
2. Checking which fingers are up
3. Matching the pattern to a number word in Filipino
4. Displaying it on screen in real time

---

##  Notes

* Designed for learning computer vision basics
* Focused on clean separation of logic (detection vs gesture rules)
* Works best with good lighting and a clear camera view
