import streamlit as st
import os
import random
from PIL import Image

with st.expander("Gallery Without Prompt（展开项目说明）"):
    st.write("本项目展示的图片生成流程为：使用Flux.1 dev生成720p图片再使用Flux.1 schnell图生图生成1440p图片，在生成时不填写提示词。这样生成效果优于直接使用Flux.1 schnell，分辨率优于直接使用Flux.1 dev。图片有16：9和9：16两种宽高比，选择宽高比后随机显示图片。")
    
# 创建下拉菜单和刷新按钮
col1, col2 = st.columns([1, 10],vertical_alignment="bottom")
with col1:
    refresh_button = st.button("🔄")
with col2:
    aspect_ratio = st.selectbox("选择图片比例", ["16:9", "9:16"], index=0)

# 定义图片路径
image_dir_16_9 = "16：9"
image_dir_9_16 = "9：16"

# 获取图片列表
def get_image_list(folder):
    if os.path.exists(folder):
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return []

# 随机选择20张图片
def select_random_images(image_list, num_images=20):
    if len(image_list) >= num_images:
        return random.sample(image_list, num_images)
    return image_list

# 显示图片
def display_images(image_list, columns=1):
    if columns == 1:
        for img_path in image_list:
            st.image(img_path)
    else:
        cols = st.columns(columns)
        for i, img_path in enumerate(image_list):
            cols[i % columns].image(img_path)

# 根据选择的比例显示图片
if aspect_ratio == "16:9":
    image_list = get_image_list(image_dir_16_9)
    if refresh_button or not st.session_state.get('16:9_images'):
        st.session_state['16:9_images'] = select_random_images(image_list)
    display_images(st.session_state['16:9_images'])
else:
    image_list = get_image_list(image_dir_9_16)
    if refresh_button or not st.session_state.get('9:16_images'):
        st.session_state['9:16_images'] = select_random_images(image_list)
    display_images(st.session_state['9:16_images'], columns=2)
