"""
tests/test_gesture.py — Unit tests for FingerState.

Run with:  pytest tests/ -v
"""

import pytest
from unittest.mock import MagicMock

from hand_tracker.gesture import FingerState
from hand_tracker.config import GestureConfig, FILIPINO_NUMBERS


# ──────────────────────────────────────────────────────────────────────────────
#  Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _make_landmark(x: float = 0.5, y: float = 0.5, z: float = 0.0) -> MagicMock:
    lm = MagicMock()
    lm.x = x
    lm.y = y
    lm.z = z
    return lm


def _make_hand(
    *,
    thumb_up: bool = False,
    index_up: bool = False,
    middle_up: bool = False,
    ring_up: bool = False,
    pinky_up: bool = False,
) -> list[MagicMock]:
    """
    Build a minimal 21-landmark list that encodes the requested finger states.

    We only need to satisfy the comparison conditions inside FingerState.
    Landmarks not involved in a specific finger's check default to (0.5, 0.5).
    """
    lm = [_make_landmark() for _ in range(21)]

    # ── thumb (indices 1-4) ─────────────────────────────────────────
    # THUMB_CMC=1, THUMB_MCP=2, THUMB_IP=3, THUMB_TIP=4
    if thumb_up:
        # tip.x < IP.x  AND  abs(tip.y - CMC.y) >= tolerance
        lm[4].x = 0.2   # tip
        lm[3].x = 0.4   # IP  → tip < IP ✓
        lm[1].y = 0.9   # CMC (far from tip.y = 0.5) → |0.5 - 0.9| = 0.4 >= 0.1
    else:
        # tip.x >= IP.x  (not extended laterally)
        lm[4].x = 0.6
        lm[3].x = 0.4

    # ── helper: set tip above (lower y) or below (higher y) PIP ────
    def _set_finger(tip_idx: int, pip_idx: int, up: bool) -> None:
        lm[tip_idx].y = 0.2 if up else 0.8   # up → tip high in frame
        lm[pip_idx].y = 0.5                   # PIP always mid-frame

    _set_finger(8,  6,  index_up)
    _set_finger(12, 10, middle_up)
    _set_finger(16, 14, ring_up)
    _set_finger(20, 18, pinky_up)

    return lm


# ──────────────────────────────────────────────────────────────────────────────
#  Tests
# ──────────────────────────────────────────────────────────────────────────────

class TestFingerState:

    def _fs(self, **kwargs) -> FingerState:
        return FingerState(_make_hand(**kwargs), GestureConfig())

    # ── individual fingers ──────────────────────────────────────────

    def test_all_down_is_zero(self):
        fs = self._fs()
        assert fs.state == (0, 0, 0, 0, 0)

    def test_index_only(self):
        fs = self._fs(index_up=True)
        assert fs.state == (0, 1, 0, 0, 0)

    def test_index_and_middle(self):
        fs = self._fs(index_up=True, middle_up=True)
        assert fs.state == (0, 1, 1, 0, 0)

    def test_thumb_only(self):
        fs = self._fs(thumb_up=True)
        assert fs.state[0] == 1
        assert fs.state[1:] == (0, 0, 0, 0)

    def test_all_up_is_lima(self):
        fs = self._fs(
            thumb_up=True,
            index_up=True,
            middle_up=True,
            ring_up=True,
            pinky_up=True,
        )
        assert fs.state == (1, 1, 1, 1, 1)

    # ── label mapping ───────────────────────────────────────────────

    @pytest.mark.parametrize("state, expected_label", [
        ((0, 0, 0, 0, 0), "Wala"),
        ((0, 1, 0, 0, 0), "Isa"),
        ((0, 1, 1, 0, 0), "Dalawa"),
        ((0, 1, 1, 1, 0), "Tatlo"),
        ((0, 1, 1, 1, 1), "Apat"),
        ((1, 1, 1, 1, 1), "Lima"),
    ])
    def test_label_matches_config(self, state, expected_label):
        assert FILIPINO_NUMBERS[state] == expected_label

    def test_unknown_gesture_returns_empty_label(self):
        # pinky only — not in the mapping
        fs = self._fs(pinky_up=True)
        assert fs.label == ""