"""
handtracker — Filipino number gesture recognition via MediaPipe.

Public surface:
    HandDetector   — wraps MediaPipe HandLandmarker
    FingerState    — pure finger-extension logic
    HandRenderer   — OpenCV drawing helpers
    DetectorConfig / GestureConfig / RendererConfig — dataclass settings
"""

import os, sys

# Ensure the project root is on sys.path so sub-module imports resolve
# correctly regardless of how/where Python was launched.
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from handtracker.config import DetectorConfig, GestureConfig, RendererConfig
from handtracker.detector import HandDetector
from handtracker.gesture import FingerState
from handtracker.renderer import HandRenderer

__all__ = [
    "HandDetector",
    "FingerState",
    "HandRenderer",
    "DetectorConfig",
    "GestureConfig",
    "RendererConfig",
]