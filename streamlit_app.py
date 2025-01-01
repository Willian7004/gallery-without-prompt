import os
import random
import streamlit as st
from PIL import Image

with st.expander("Gallery Without Prompt（展开项目说明）"):
    st.write("本项目展示的图片生成流程为：使用Flux.1 dev生成720p图片再使用Flux.1 schnell图生图生成1440p图片，在生成时不填写提示词。这样生成效果优于直接使用Flux.1 schnell，分辨率优于直接使用Flux.1 dev。图片有16：9和9：16两种宽高比，选择宽高比后随机显示图片。")
   
# 创建文件夹路径
folder_16_9 = "16：9"
folder_9_16 = "9：16"

# 确保文件夹存在
if not os.path.exists(folder_16_9):
    os.makedirs(folder_16_9)
if not os.path.exists(folder_9_16):
    os.makedirs(folder_9_16)

# 获取文件夹中的所有图片文件
def get_images(folder):
    images = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return images

# 随机选择20张图片
def select_random_images(images, count=20):
    return random.sample(images, min(count, len(images)))

# 显示图片并添加下载按钮
def display_images(images, show_download_button, columns=1):
    if columns == 1:
        for img_path in images:
            img = Image.open(img_path)
            st.image(img)
            if show_download_button:
                with open(img_path, "rb") as file:
                    btn = st.download_button(
                        label="下载图片",
                        data=file,
                        file_name=os.path.basename(img_path),
                        mime="image/jpeg"
                    )
    else:
        cols = st.columns(columns)
        for i, img_path in enumerate(images):
            img = Image.open(img_path)
            cols[i % columns].image(img)
            if show_download_button:
                with open(img_path, "rb") as file:
                    btn = cols[i % columns].download_button(
                        label="下载图片",
                        data=file,
                        file_name=os.path.basename(img_path),
                        mime="image/jpeg"
                    )


# 在同一行创建按钮、下拉菜单和复选框
col1, col2, col3 = st.columns([2, 9,3],vertical_alignment="bottom")
with col1:
    refresh_button = st.button("🔄 刷新")
with col2:
    aspect_ratio = st.selectbox("选择图片比例", ["16：9", "9：16"], index=0)
with col3:
    show_download_button = st.checkbox("显示下载按钮")

# 根据下拉菜单的选择加载图片
if aspect_ratio == "16：9":
    images = get_images(folder_16_9)
    display_columns = 1
else:
    images = get_images(folder_9_16)
    display_columns = 2

# 随机选择20张图片并显示
selected_images = select_random_images(images)
display_images(selected_images, show_download_button, display_columns)
