# 🖐️ Hand Tracking — Filipino Number Recognition

Real-time hand gesture recognition using **MediaPipe HandLandmarker** and **OpenCV**, with gestures mapped to Filipino (Tagalog) number words.

| Fingers Up | Label |
|---|---|
| ✊ none | **Wala** |
| ☝️ index | **Isa** |
| ✌️ index + middle | **Dalawa** |
| 🤟 index + middle + ring | **Tatlo** |
| 🖖 index + middle + ring + pinky | **Apat** |
| 🖐️ all five | **Lima** |

---

## Project Structure

```
hand-tracking/
├── hand_tracker/
│   ├── __init__.py      # Public API surface
│   ├── config.py        # All tunable constants (dataclasses)
│   ├── detector.py      # MediaPipe HandLandmarker wrapper
│   ├── gesture.py       # Pure finger-state logic (no OpenCV)
│   └── renderer.py      # OpenCV drawing helpers
├── tests/
│   └── test_gesture.py  # Unit tests (pytest)
├── main.py              # Entry point with argparse
├── requirements.txt
└── .gitignore
```

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/joreese-clyde/hand-tracking.git
cd hand-tracking
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the MediaPipe model
```bash
curl -o hand_landmarker.task \
  "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
```

### 5. Run
```bash
python main.py
```

Press **ESC** to quit.

---

## CLI Options

```
python main.py [--camera N] [--num-hands N] [--no-fps] [--no-skeleton]

  --camera N        Camera device index (default: 0)
  --num-hands N     Max hands to detect (default: 2)
  --no-fps          Hide FPS counter overlay
  --no-skeleton     Hide landmark skeleton overlay
```

---

## Running Tests

```bash
pytest tests/ -v
```

To check code coverage:
```bash
pytest tests/ --cov=hand_tracker --cov-report=term-missing
```

---

## Configuration

All constants (thresholds, colours, font size, etc.) live in `hand_tracker/config.py` as frozen dataclasses. Override them at runtime by passing a custom config object to any class constructor:

```python
from hand_tracker import HandDetector, DetectorConfig

cfg = DetectorConfig(num_hands=1, min_hand_detection_confidence=0.8)
with HandDetector(cfg) as detector:
    ...
```

---

## Requirements

- Python ≥ 3.10
- A webcam or USB camera
- MediaPipe `hand_landmarker.task` model (see step 4 above)

---

## License

MIT — see [LICENSE](LICENSE) for details.