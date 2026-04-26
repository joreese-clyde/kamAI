"""ht_gesture.py — Finger-state logic. No OpenCV dependency."""
from ht_config import GestureConfig, FILIPINO_NUMBERS

# Landmark indices
THUMB_CMC, THUMB_IP, THUMB_TIP = 1, 3, 4
INDEX_TIP,  INDEX_PIP  = 8,  6
MIDDLE_TIP, MIDDLE_PIP = 12, 10
RING_TIP,   RING_PIP   = 16, 14
PINKY_TIP,  PINKY_PIP  = 20, 18

class FingerState:
    """Computes which fingers are extended for a single detected hand."""

    def __init__(self, landmarks, config: GestureConfig | None = None):
        self._lm  = landmarks
        self._cfg = config or GestureConfig()
        self._state: tuple = self._compute()

    @property
    def state(self) -> tuple:
        return self._state

    @property
    def label(self) -> str:
        return FILIPINO_NUMBERS.get(self._state, "")

    def _compute(self) -> tuple:
        lm = self._lm
        return (
            int(self._thumb_up(lm)),
            int(lm[INDEX_TIP].y  < lm[INDEX_PIP].y),
            int(lm[MIDDLE_TIP].y < lm[MIDDLE_PIP].y),
            int(lm[RING_TIP].y   < lm[RING_PIP].y),
            int(lm[PINKY_TIP].y  < lm[PINKY_PIP].y),
        )

    def _thumb_up(self, lm) -> bool:
        x_ok  = lm[THUMB_TIP].x < lm[THUMB_IP].x
        y_far = abs(lm[THUMB_TIP].y - lm[THUMB_CMC].y) >= self._cfg.thumb_y_tolerance
        return x_ok and y_far