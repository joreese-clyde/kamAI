"""ht_detector.py — Thin MediaPipe HandLandmarker wrapper."""
import logging
from pathlib import Path

import mediapipe as mp
import numpy as np

from ht_config import DetectorConfig

logger = logging.getLogger(__name__)

_BaseOptions        = mp.tasks.BaseOptions
_HandLandmarker     = mp.tasks.vision.HandLandmarker
_HandLandmarkerOpts = mp.tasks.vision.HandLandmarkerOptions
_RunningMode        = mp.tasks.vision.RunningMode


class HandDetector:
    """Context-manager wrapper around MediaPipe HandLandmarker."""

    def __init__(self, config: DetectorConfig | None = None):
        self._cfg = config or DetectorConfig()
        self._lm  = None
        self._init()

    def __enter__(self):  return self
    def __exit__(self, *_): self.close()

    def detect(self, bgr_frame: np.ndarray):
        if self._lm is None:
            raise RuntimeError("HandDetector is closed.")
        rgb = bgr_frame[:, :, ::-1]          # BGR → RGB
        img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        return self._lm.detect(img)

    def close(self):
        if self._lm:
            self._lm.close()
            self._lm = None

    def _init(self):
        path = Path(self._cfg.model_path)
        if not path.exists():
            raise FileNotFoundError(
                f"\n Model not found: {path}\n"
                "Download it with:\n"
                "  curl -o hand_landmarker.task https://storage.googleapis.com/"
                "mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
            )
        opts = _HandLandmarkerOpts(
            base_options=_BaseOptions(model_asset_path=str(path)),
            running_mode=_RunningMode.IMAGE,
            num_hands=self._cfg.num_hands,
            min_hand_detection_confidence=self._cfg.min_hand_detection_confidence,
            min_hand_presence_confidence=self._cfg.min_hand_presence_confidence,
            min_tracking_confidence=self._cfg.min_tracking_confidence,
        )
        self._lm = _HandLandmarker.create_from_options(opts)
        logger.info("HandDetector ready — %s", path.name)