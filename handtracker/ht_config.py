"""ht_config.py — All tunable constants."""
from dataclasses import dataclass
from pathlib import Path

ROOT_DIR   = Path(__file__).resolve().parent
MODEL_PATH = ROOT_DIR / "hand_landmarker.task"

@dataclass(frozen=True)
class DetectorConfig:
    model_path: Path = MODEL_PATH
    num_hands: int = 2
    min_hand_detection_confidence: float = 0.6
    min_hand_presence_confidence: float = 0.6
    min_tracking_confidence: float = 0.5

@dataclass(frozen=True)
class GestureConfig:
    thumb_y_tolerance: float = 0.10

@dataclass(frozen=True)
class RendererConfig:
    window_title: str       = "Hand Tracker — ESC to quit"
    landmark_radius: int    = 4
    landmark_color: tuple   = (0, 255, 0)
    connection_color: tuple = (255, 255, 255)
    connection_thickness: int = 2
    label_color: tuple      = (0, 255, 0)
    label_font_scale: float = 1.8
    label_thickness: int    = 3
    label_origin: tuple     = (30, 90)
    flip_horizontal: bool   = True

FILIPINO_NUMBERS: dict = {
    (0, 0, 0, 0, 0): "Wala",
    (0, 1, 0, 0, 0): "Isa",
    (0, 1, 1, 0, 0): "Dalawa",
    (0, 1, 1, 1, 0): "Tatlo",
    (0, 1, 1, 1, 1): "Apat",
    (1, 1, 1, 1, 1): "Lima",
}