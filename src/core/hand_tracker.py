# core/hand_tracker.py

import cv2
import mediapipe as mp


class FingerCounter:
    FINGER_TIPS = [4, 8, 12, 16, 20]
    FINGER_BASES = [2, 5, 9, 13, 17]

    def __init__(self):
        """Initialize MediaPipe Hands."""

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_styles = mp.solutions.drawing_styles

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = self.hands.process(rgb)

        annotated = frame.copy()

        if not res.multi_hand_landmarks:
            return -1, 0, 0.0, annotated

        total_fingers = 0
        all_conf = []

        for hand_lm, hand_info in zip(
            res.multi_hand_landmarks,
            res.multi_handedness,
        ):
            conf = hand_info.classification[0].score
            all_conf.append(conf)

            label = hand_info.classification[0].label
            lm = hand_lm.landmark

            count = 0

            # Thumb detection
            if label == "Right":
                if lm[4].x < lm[3].x:
                    count += 1
            else:
                if lm[4].x > lm[3].x:
                    count += 1

            # Other fingers
            for tip, base in zip(
                self.FINGER_TIPS[1:],
                self.FINGER_BASES[1:]
            ):
                if lm[tip].y < lm[base].y:
                    count += 1

            total_fingers += count

            # Draw landmarks
            self.mp_draw.draw_landmarks(
                annotated,
                hand_lm,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_styles.get_default_hand_landmarks_style(),
                self.mp_styles.get_default_hand_connections_style(),
            )

        return (
            min(total_fingers, 10),
            len(res.multi_hand_landmarks),
            float(sum(all_conf) / len(all_conf)),
            annotated,
        )

    def release(self):
        self.hands.close()