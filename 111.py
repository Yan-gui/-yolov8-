#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()
print(file_path)
# Get the parent directory of the current file
root_path = file_path.parent
print(root_path)

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Source
SOURCES_LIST = ["图片", "摄像头"]

print(root_path)
# DL model config
DETECTION_MODEL_DIR = root_path / 'weights'
print(DETECTION_MODEL_DIR)
YOLOv8n = DETECTION_MODEL_DIR / "best.pt"
print(YOLOv8n)
# YOLOv8s = DETECTION_MODEL_DIR / "yolov8s.pt"
# YOLOv8m = DETECTION_MODEL_DIR / "yolov8m.pt"
# YOLOv8l = DETECTION_MODEL_DIR / "yolov8l.pt"
# YOLOv8x = DETECTION_MODEL_DIR / "yolov8x.pt"

DETECTION_MODEL_LIST = ["best.pt", ]
