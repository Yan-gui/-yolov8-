# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# from ultralytics import YOLO
# import streamlit as st
# import cv2
# from PIL import Image
# import tempfile
#
#
# def _display_detected_frames(conf, model, st_frame, image):
#     """
#     Display the detected objects on a video frame using the YOLOv8 model.
#     :param conf (float): Confidence threshold for object detection.
#     :param model (YOLOv8): An instance of the `YOLOv8` class containing the YOLOv8 model.
#     :param st_frame (Streamlit object): A Streamlit object to display the detected video.
#     :param image (numpy array): A numpy array representing the video frame.
#     :return: None
#     """
#     # Resize the image to a standard size
#     image = cv2.resize(image, (720, int(720 * (9 / 16))))
#
#     # Predict the objects in the image using YOLOv8 model
#     res = model.predict(image, conf=conf)
#
#     # Plot the detected objects on the video frame
#     res_plotted = res[0].plot()
#     st_frame.image(res_plotted,
#                    caption='Detected Video',
#                    channels="BGR",
#                    use_column_width=True
#                    )
#
#
# @st.cache_resource
# def load_model(model_path):
#     """
#     Loads a YOLO object detection model from the specified model_path.
#
#     Parameters:
#         model_path (str): The path to the YOLO model file.
#
#     Returns:
#         A YOLO object detection model.
#     """
#     model = YOLO(model_path)
#     return model
#
#
# def infer_uploaded_image(conf, model):
#     """
#     Execute inference for uploaded image
#     :param conf: Confidence of YOLOv8 model
#     :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
#     :return: None
#     """
#     source_img = st.sidebar.file_uploader(
#         label="选择一张图片...",
#         type=("jpg", "jpeg", "png", 'bmp', 'webp')
#     )
#
#     col1, col2 = st.columns(2)
#
#     with col1:
#         if source_img:
#             uploaded_image = Image.open(source_img)
#             # adding the uploaded image to the page with caption
#             st.image(
#                 image=source_img,
#                 caption="被上传图像",
#                 use_column_width=True
#             )
#
#     if source_img:
#         if st.button("开始识别"):
#             with st.spinner("运行中..."):
#                 res = model.predict(uploaded_image,
#                                     conf=conf)
#                 boxes = res[0].boxes
#                 res_plotted = res[0].plot()[:, :, ::-1]
#
#                 with col2:
#                     st.image(res_plotted,
#                              caption="检测到的图像",
#                              use_column_width=True)
#                     try:
#                         with st.expander("识别结果"):
#                             for box in boxes:
#                                 st.write(box.xywh)
#                     except Exception as ex:
#                         st.write("还没有上传图片!")
#                         st.write(ex)
#
#
# def infer_uploaded_webcam(conf, model):
#     """
#     Execute inference for webcam.
#     :param conf: Confidence of YOLOv8 model
#     :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
#     :return: None
#     """
#     try:
#         flag = st.button(
#             label="停止运行"
#         )
#         vid_cap = cv2.VideoCapture(0)  # local camera
#         st_frame = st.empty()
#         while not flag:
#             success, image = vid_cap.read()
#             if success:
#                 _display_detected_frames(
#                     conf,
#                     model,
#                     st_frame,
#                     image
#                 )
#             else:
#                 vid_cap.release()
#                 break
#     except Exception as e:
#         st.error(f"Error loading video: {str(e)}")





# 加了视频后的：
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import streamlit as st
import cv2
import tempfile
import os
from ultralytics import YOLO
from PIL import Image

@st.cache_resource
def load_model(model_path):
    """
    加载 YOLO 模型
    """
    model = YOLO(model_path)
    return model

def _display_detected_frames(conf, model, st_frame, image):
    """
    逐帧显示YOLOv8检测结果
    """
    image = cv2.resize(image, (720, int(720 * (9 / 16))))
    res = model.predict(image, conf=conf)
    res_plotted = res[0].plot()
    st_frame.image(res_plotted, caption='检测结果', channels="BGR", use_column_width=True)

def infer_uploaded_image(conf, model):
    """
    执行上传图片的目标检测
    """
    source_img = st.sidebar.file_uploader("选择一张图片...", type=("jpg", "jpeg", "png", "bmp", "webp"))

    col1, col2 = st.columns(2)

    with col1:
        if source_img:
            uploaded_image = Image.open(source_img)
            st.image(uploaded_image, caption="被上传图像", use_column_width=True)

    if source_img and st.button("开始识别"):
        with st.spinner("运行中..."):
            res = model.predict(uploaded_image, conf=conf)
            res_plotted = res[0].plot()[:, :, ::-1]

            with col2:
                st.image(res_plotted, caption="检测到的图像", use_column_width=True)
                with st.expander("识别结果"):
                    for box in res[0].boxes:
                        st.write(box.xywh)

def infer_uploaded_webcam(conf, model):
    """
    执行摄像头的目标检测
    """
    try:
        flag = st.button("停止运行")
        vid_cap = cv2.VideoCapture(0)
        st_frame = st.empty()
        while not flag:
            success, image = vid_cap.read()
            if success:
                _display_detected_frames(conf, model, st_frame, image)
            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"摄像头加载出错: {str(e)}")

def infer_uploaded_video(conf, model):
    """
    执行上传视频的目标检测
    """
    source_video = st.sidebar.file_uploader("上传视频文件...", type=("mp4", "avi", "mov", "mkv"))

    if source_video:
        # 临时存储视频
        temp_dir = tempfile.TemporaryDirectory()
        temp_video_path = os.path.join(temp_dir.name, source_video.name)

        with open(temp_video_path, "wb") as f:
            f.write(source_video.read())

        # 显示上传的视频
        st.video(temp_video_path)

        if st.button("开始视频检测"):
            with st.spinner("视频处理中，请稍等..."):
                cap = cv2.VideoCapture(temp_video_path)
                st_frame = st.empty()

                while cap.isOpened():
                    success, frame = cap.read()
                    if not success:
                        break

                    _display_detected_frames(conf, model, st_frame, frame)

                cap.release()

        temp_dir.cleanup()


