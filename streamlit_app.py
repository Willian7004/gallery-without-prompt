import streamlit as st
import os
import random
from PIL import Image

# 设置页面布局为宽模式
st.set_page_config(layout="wide")

# 获取当前目录下的文件夹
folders = {"16:9": "16：9", "9:16": "9：16"}
available_folders = {k: v for k, v in folders.items() if os.path.isdir(v)}

# 检查必要文件夹是否存在
if "16:9" not in available_folders and "9:16" not in available_folders:
    st.error("当前目录下没有名为 '16:9' 或 '9:16' 的文件夹。")
    st.stop()

#项目说明
with st.expander("Gallery Without Prompt（展开项目说明）"):
        st.write("本项目展示的图片生成流程为：使用Flux.1 dev生成720p图片再使用Flux.1 schnell图生图生成1440p图片，在生成时不填写提示词。这样生成效果优于直接使用Flux.1 schnell，分辨率优于直接使用Flux.1 dev。图片有16：9和9：16两种宽高比，选择宽高比后随机显示图片。")
        st.write("当前为第二版，由于第一版因风格不明确导致出片率较低，本版本改为使用3种风格提示词分别生成。照片风格主要排除了光照或材质有问题的图片。动漫风格相比完整提示词，生成的图片风格接近手绘。油画风格生成的实际风格有一部分是旧模型的风格或纹理异常，也排除了这一部分。总体质量和出片率明显优于第一版。可以在release中找到历史版本。")
        st.write("第二版的逻辑功能也进行了调整，加大了页面宽度，改为双列显示16：9图片，分四列显示9：16图片。")

# 创建并排放置的列
col1, col2, col3, col4 = st.columns([1, 6, 5, 2],vertical_alignment="bottom")

# 按钮：刷新图标
with col1:
    refresh = st.button("🔄刷新", key="refresh_button", help="点击刷新图片")

# 第一个下拉菜单：选择比例
with col2:
    aspect_ratio = st.selectbox("选择图片比例", ["16:9", "9:16"], index=0, key="aspect_ratio")

# 第二个下拉菜单：选择文件夹
with col3:
    # 获取第一步选择的文件夹下的所有子文件夹
    main_folder = folders[aspect_ratio]
    sub_folders = [f for f in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, f))]
    folder_options = ["全部"] + sub_folders
    selected_folder = st.selectbox("选择图片风格", folder_options, index=0, key="selected_folder")

# 复选框：显示下载按钮
with col4:
    show_download = st.checkbox("显示下载按钮", value=False, key="show_download")

# 根据选择的文件夹和子文件夹获取图片路径
def get_image_paths(main_folder, selected_folder):
    if selected_folder == "全部":
        image_paths = []
        for sub_folder in sub_folders:
            folder_path = os.path.join(main_folder, sub_folder)
            images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith((".png", ".jpg", ".jpeg"))]
            image_paths.extend(images)
    else:
        folder_path = os.path.join(main_folder, selected_folder)
        image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith((".png", ".jpg", ".jpeg"))]
    return image_paths

image_paths = get_image_paths(main_folder, selected_folder)

# 随机选择20张图片
if image_paths:
    if len(image_paths) < 20:
        st.warning(f"文件夹中图片不足20张，共找到 {len(image_paths)} 张图片。")
        selected_images = image_paths
    else:
        selected_images = random.sample(image_paths, 20)
else:
    st.warning("未找到图片，请检查文件夹路径。")
    st.stop()

# 根据比例分列显示图片
if aspect_ratio == "16:9":
    cols = st.columns(2)
elif aspect_ratio == "9:16":
    cols = st.columns(4)
else:
    cols = st.columns(2)  # 默认两列

# 显示图片和下载按钮
for i, img_path in enumerate(selected_images):
    col = cols[i % len(cols)]
    with col:
        img = Image.open(img_path)
        st.image(img)
        if show_download:
            with open(img_path, "rb") as f:
                btn = st.download_button(
                    label="下载",
                    data=f,
                    file_name=os.path.basename(img_path),
                    mime="image/png"
                )
