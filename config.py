# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# from pathlib import Path
# import sys
#
# # Get the absolute path of the current file
# file_path = Path(__file__).resolve()
#
# # Get the parent directory of the current file
# root_path = file_path.parent
#
# # Add the root path to the sys.path list if it is not already there
# if root_path not in sys.path:
#     sys.path.append(str(root_path))
#
# # Get the relative path of the root directory with respect to the current working directory
# ROOT = root_path.relative_to(Path.cwd())
#
#
# # Source
# SOURCES_LIST = ["图片", "摄像头"]
#
#
# # DL model config
# DETECTION_MODEL_DIR = ROOT / 'weights'
# YOLOv8n = DETECTION_MODEL_DIR / "best.pt"
# # YOLOv8s = DETECTION_MODEL_DIR / "yolov8s.pt"
# # YOLOv8m = DETECTION_MODEL_DIR / "yolov8m.pt"
# # YOLOv8l = DETECTION_MODEL_DIR / "yolov8l.pt"
# # YOLOv8x = DETECTION_MODEL_DIR / "yolov8x.pt"
#
# DETECTION_MODEL_LIST = ["best.pt", ]






# 加了视频后的：
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from pathlib import Path
# import sys
#
# # 获取当前文件的绝对路径
# file_path = Path(__file__).resolve()
#
# # 获取当前文件的父目录
# root_path = file_path.parent
#
# # 将 root_path 添加到 sys.path
# if root_path not in sys.path:
#     sys.path.append(str(root_path))
#
# # 获取相对路径
# ROOT = root_path.relative_to(Path.cwd())
#
# # 数据来源选项（增加视频）
# SOURCES_LIST = ["图片", "摄像头", "视频"]  # 添加 "视频" 选项
#
# # 深度学习模型配置
# DETECTION_MODEL_DIR = ROOT / 'weights'
# YOLOv8n = DETECTION_MODEL_DIR / "best-3.pt"
#
# DETECTION_MODEL_LIST = ["best-3.pt"]
#



from pathlib import Path

# 模型存放的目录
DETECTION_MODEL_DIR = Path("weights")

# 获取所有 .pt 文件的模型列表
DETECTION_MODEL_LIST = [model.name for model in DETECTION_MODEL_DIR.glob("*.pt")]

# 数据来源选项（图片、摄像头、视频）
SOURCES_LIST = ["图片", "摄像头", "视频"]  # 添加 "视频" 选项
