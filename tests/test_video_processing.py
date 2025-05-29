import pytest
from src.video_processing import extract_key_frames

def test_extract_key_frames():
    frames = extract_key_frames("non_existent_video.mp4")
    assert frames == []  # Should handle missing file gracefully
