"""ht_renderer.py — All OpenCV drawing logic."""
import cv2
import numpy as np
from ht_config import RendererConfig

HAND_CONNECTIONS = (
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (0,9),(9,10),(10,11),(11,12),
    (0,13),(13,14),(14,15),(15,16),
    (0,17),(17,18),(18,19),(19,20),
    (5,9),(9,13),(13,17),
)

class HandRenderer:
    def __init__(self, config: RendererConfig | None = None):
        self._cfg = config or RendererConfig()

    def draw_landmarks(self, frame: np.ndarray, landmarks) -> None:
        h, w = frame.shape[:2]
        pts = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]
        for a, b in HAND_CONNECTIONS:
            cv2.line(frame, pts[a], pts[b],
                     self._cfg.connection_color,
                     self._cfg.connection_thickness, cv2.LINE_AA)
        for pt in pts:
            cv2.circle(frame, pt, self._cfg.landmark_radius,
                       self._cfg.landmark_color, -1, cv2.LINE_AA)

    def draw_label(self, frame: np.ndarray, label: str) -> None:
        if not label:
            return
        text, org = f"Bilang: {label}", self._cfg.label_origin
        # shadow
        cv2.putText(frame, text, (org[0]+2, org[1]+2),
                    cv2.FONT_HERSHEY_DUPLEX, self._cfg.label_font_scale,
                    (0,0,0), self._cfg.label_thickness + 1, cv2.LINE_AA)
        cv2.putText(frame, text, org,
                    cv2.FONT_HERSHEY_DUPLEX, self._cfg.label_font_scale,
                    self._cfg.label_color, self._cfg.label_thickness, cv2.LINE_AA)

    def draw_fps(self, frame: np.ndarray, fps: float) -> None:
        h, w = frame.shape[:2]
        text = f"FPS: {fps:.1f}"
        (tw, _), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.putText(frame, text, (w - tw - 10, 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (200,200,200), 1, cv2.LINE_AA)