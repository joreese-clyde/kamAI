"""
main.py — Hand Tracking entry point (Filipino number recognition).

Usage:
    python main.py
    python main.py --camera 1
    python main.py --no-fps
    python main.py --no-skeleton
"""

from __future__ import annotations
import argparse, logging, sys, time
from pathlib import Path

# ── guarantee local modules are always found first ──────────────────────────
sys.path.insert(0, str(Path(__file__).resolve().parent))
# ────────────────────────────────────────────────────────────────────────────

import cv2
from ht_config   import DetectorConfig, GestureConfig, RendererConfig
from ht_detector import HandDetector
from ht_gesture  import FingerState
from ht_renderer import HandRenderer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger  = logging.getLogger(__name__)
ESC_KEY = 27


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Filipino number gesture recognition — MediaPipe + OpenCV",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--camera",     "-c", type=int, default=0, help="Camera index")
    p.add_argument("--num-hands",  "-n", type=int, default=2, help="Max hands")
    p.add_argument("--no-fps",     action="store_true", help="Hide FPS overlay")
    p.add_argument("--no-skeleton",action="store_true", help="Hide skeleton")
    return p.parse_args()


def open_camera(idx: int) -> cv2.VideoCapture:
    cap = cv2.VideoCapture(idx)
    if not cap.isOpened():
        logger.error("Cannot open camera %d", idx); sys.exit(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    logger.info("Camera %d  —  %dx%d", idx,
                int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    return cap


def run(args: argparse.Namespace) -> None:
    det_cfg  = DetectorConfig(num_hands=args.num_hands)
    gest_cfg = GestureConfig()
    rend_cfg = RendererConfig()

    cap      = open_camera(args.camera)
    renderer = HandRenderer(rend_cfg)
    prev_t   = time.perf_counter()

    with HandDetector(det_cfg) as detector:
        logger.info("Running — press ESC to quit.")
        while True:
            ret, frame = cap.read()
            if not ret:
                logger.warning("Empty frame — retrying…"); continue

            if rend_cfg.flip_horizontal:
                frame = cv2.flip(frame, 1)

            result     = detector.detect(frame)
            last_label = ""

            if result.hand_landmarks:
                for hand_lm in result.hand_landmarks:
                    fs         = FingerState(hand_lm, gest_cfg)
                    last_label = fs.label
                    if not args.no_skeleton:
                        renderer.draw_landmarks(frame, hand_lm)

            renderer.draw_label(frame, last_label)

            if not args.no_fps:
                now    = time.perf_counter()
                fps    = 1.0 / max(now - prev_t, 1e-9)
                prev_t = now
                renderer.draw_fps(frame, fps)

            cv2.imshow(rend_cfg.window_title, frame)
            if cv2.waitKey(1) & 0xFF == ESC_KEY:
                logger.info("ESC — exiting."); break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run(parse_args())