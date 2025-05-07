# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# from pathlib import Path
# from PIL import Image
# import streamlit as st
#
# import config
# from utils import load_model, infer_uploaded_image, infer_uploaded_webcam
#
# # setting page layout
# st.set_page_config(
#     page_title="Interactive Interface for YOLOv8",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded"
#     )
#
# # main page heading
# st.title("YOLO交通目标检测系统")
#
# # sidebar
# st.sidebar.header("模型配置")
#
# # model options
# task_type = st.sidebar.selectbox(
#     "选择任务",
#     ["Detection"]
# )
#
# model_type = None
# if task_type == "Detection":
#     model_type = st.sidebar.selectbox(
#         "选择模型",
#         config.DETECTION_MODEL_LIST
#     )
# else:
#     st.error("Currently only 'Detection' function is implemented")
#
# confidence = float(st.sidebar.slider(
#     "设置模型置信度阈值", 30, 100, 50)) / 100
#
# model_path = ""
# if model_type:
#     model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
# else:
#     st.error("Please Select Model in Sidebar")
#
# # load pretrained DL model
# try:
#     model = load_model(model_path)
# except Exception as e:
#     st.error(f"Unable to load model. Please check the specified path: {model_path}")
#
# # image/video options
# st.sidebar.header("图片/摄像头 配置")
# source_selectbox = st.sidebar.selectbox(
#     "选择文件类型",
#     config.SOURCES_LIST
# )
#
# source_img = None
# if source_selectbox == config.SOURCES_LIST[0]: # Image
#     infer_uploaded_image(confidence, model)
# elif source_selectbox == config.SOURCES_LIST[1]: # Webcam
#     infer_uploaded_webcam(confidence, model)
# else:
#     st.error("Currently only 'Image' and 'Video' source are implemented")






# 加了视频后的：
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import streamlit as st  # 确保 set_page_config 是第一个 Streamlit 相关调用
# from pathlib import Path
# from PIL import Image
#
# import config
# from utils import load_model, infer_uploaded_image, infer_uploaded_webcam, infer_uploaded_video
#
# # ✅ set_page_config 必须是第一个 Streamlit 语句
# st.set_page_config(
#     page_title="YOLO交通目标检测系统",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
#
# # 主标题
# st.title("YOLO交通目标检测系统")
#
# # 侧边栏 - 模型配置
# st.sidebar.header("模型配置")
#
# # 选择任务类型
# task_type = st.sidebar.selectbox(
#     "选择任务",
#     ["Detection"]
# )
#
# model_type = None
# if task_type == "Detection":
#     model_type = st.sidebar.selectbox(
#         "选择模型",
#         config.DETECTION_MODEL_LIST
#     )
# else:
#     st.error("目前仅支持 'Detection' 任务")
#
# # 置信度选择
# confidence = float(st.sidebar.slider(
#     "设置模型置信度阈值", 30, 100, 50)) / 100
#
# # 获取模型路径
# model_path = ""
# if model_type:
#     model_path = Path(config.DETECTION_MODEL_DIR) / model_type
# else:
#     st.error("请在侧边栏选择模型")
#
# # 加载 YOLO 模型
# try:
#     model = load_model(model_path)
# except Exception as e:
#     st.error(f"无法加载模型，请检查路径是否正确: {model_path}")
#
# # 侧边栏 - 选择输入方式
# st.sidebar.header("图片/摄像头/视频 配置")
# source_selectbox = st.sidebar.selectbox(
#     "选择文件类型",
#     config.SOURCES_LIST
# )
#
# # 处理不同输入
# if source_selectbox == "图片":
#     infer_uploaded_image(confidence, model)
# elif source_selectbox == "摄像头":
#     infer_uploaded_webcam(confidence, model)
# elif source_selectbox == "视频":
#     infer_uploaded_video(confidence, model)
# else:
#     st.error("目前仅支持 图片、摄像头和视频 作为输入")



import streamlit as st  # 确保 set_page_config 是第一个 Streamlit 相关调用
from pathlib import Path
from PIL import Image

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_webcam, infer_uploaded_video

# ✅ set_page_config 必须是第一个 Streamlit 语句
st.set_page_config(
    page_title="YOLO交通目标检测系统",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 主标题
st.title("YOLO交通目标检测系统")

# 侧边栏 - 模型配置
st.sidebar.header("模型配置")

# 选择任务类型
task_type = st.sidebar.selectbox(
    "选择任务",
    ["Detection"]
)

model_type = None
if task_type == "Detection":
    # 动态加载可用模型
    model_type = st.sidebar.selectbox(
        "选择模型",
        config.DETECTION_MODEL_LIST  # 从 config 中动态加载模型列表
    )
else:
    st.error("目前仅支持 'Detection' 任务")

# 置信度选择
confidence = float(st.sidebar.slider(
    "设置模型置信度阈值", 30, 100, 50)) / 100

# 获取模型路径
model_path = ""
if model_type:
    model_path = Path(config.DETECTION_MODEL_DIR) / model_type
else:
    st.error("请在侧边栏选择模型")

# 加载 YOLO 模型
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"无法加载模型，请检查路径是否正确: {model_path}")

# 侧边栏 - 选择输入方式
st.sidebar.header("图片/摄像头/视频 配置")
source_selectbox = st.sidebar.selectbox(
    "选择文件类型",
    config.SOURCES_LIST
)

# 处理不同输入
if source_selectbox == "图片":
    infer_uploaded_image(confidence, model)
elif source_selectbox == "摄像头":
    infer_uploaded_webcam(confidence, model)
elif source_selectbox == "视频":
    infer_uploaded_video(confidence, model)
else:
    st.error("目前仅支持 图片、摄像头和视频 作为输入")
