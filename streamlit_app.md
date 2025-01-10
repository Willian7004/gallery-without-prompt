### 提示词：

使用streamlit写一个程序，实现以下功能：

1.设置layout=wide。在同一行从左到右依次创建：按钮、两个下拉菜单和一个复选框。

2.第一个下拉菜单有16：9和9：16两个选项，用于选择当前目录下同名的文件夹，默认选择16：9。

3.第二个下拉菜单第一个选项为“全部”，选中上一步选中的文件夹中所有子文件夹，并根据上一步选中的文件夹中的子文件夹名称创建其它选项用于选中对应文件夹。

4.选中文件夹后，在相应文件夹的图片中随即选择20张图片。第二步选中的文件夹为16：9则分两列显示，第二步选中的文件夹为9：16则分四列显示。

5.复选框的文字为“显示下载按钮”。选中复选框时，在每张图片下方显示下载按钮，点击下载按钮时下载相应图片。

6.按钮上为刷新图标，按下按钮时，重新随机选择20张图片并显示。

### 思维链：

好，我需要写一个Streamlit程序来实现这些功能。首先，设置布局为宽模式，这样界面会更宽，适合并排放置组件。

然后，在同一行从左到右依次创建按钮、两个下拉菜单和一个复选框。我得用Streamlit的布局功能，可能是用cols来并排放置这些组件。

第一个下拉菜单有“16:9”和“9:16”两个选项，默认选择“16:9”。我需要获取当前目录下同名的文件夹，所以可能需要检查文件夹是否存在，并且确保它们对应比例。

第二个下拉菜单第一个选项是“全部”，然后根据第一步选择的文件夹中的子文件夹名称来动态生成选项。我需要先获取第一步选择的文件夹下的所有子文件夹，然后把这些子文件夹名称作为选项。

选中文件夹后，在相应文件夹的图片中随机选择20张图片。如果第一步选的是“16:9”，就分两列显示图片；如果是“9:16”，就分四列显示。我需要根据选择来调整图片的显示布局。

复选框的文字是“显示下载按钮”，选中时在每张图片下方显示下载按钮，点击按钮可以下载相应图片。我需要在图片下方有条件地显示下载按钮，并且实现下载功能。

按钮上是刷新图标，点击时重新随机选择20张图片并显示。我需要找到一个刷新图标的按钮，可能是用FontAwesome图标来表示。

首先，我得导入Streamlit库，可能还需要导入os来处理文件路径，random来随机选择图片，PIL来处理图片，等等。

我需要定义一些变量来存储选择的状态，比如selected_ratio, selected_folder, show_download_buttons。

我得先获取当前目录下的文件夹，检查是否有“16:9”和“9:16”这两个文件夹，如果没有，可能要提示用户。

然后，设置布局为宽模式，可以用st.set_page_config(layout="wide")。

使用st.beta_columns来并排放置按钮、下拉菜单和复选框。

第一个下拉菜单可以用st.selectbox，选项是["16:9", "9:16"]，默认index=0。

第二个下拉菜单需要动态生成选项，先获取第一步选择的文件夹下的所有子文件夹，然后把这些名称作为选项，还有一个“全部”的选项在最前面。

选中文件夹后，随机选择20张图片。我需要从选中的文件夹中获取所有图片文件，然后随机选择20张。

显示图片时，根据第一步选择的比例来分列显示。如果是“16:9”，用2列；如果是“9:16”，用4列。可以用st.columns来布局。

复选框用st.checkbox，文字是“显示下载按钮”。根据这个状态来决定是否在图片下方显示下载按钮。

下载按钮可以用st.download_button，需要设置data和file_name。

刷新按钮可以用一个按钮，图标是刷新，可能是用st.button，然后在按钮点击时重新选择图片。

我需要注意状态的保持，可能需要在每次选择后重新加载图片。

可能需要一些缓存机制来优化性能，比如缓存图片加载。

还要处理一些异常情况，比如文件夹不存在，图片不足20张等等。

最好加一些注释，代码清晰易懂。

可能需要测试一下每个功能，确保都能正常工作。

好，开始写代码吧。

### 回答正文：

### 实现步骤

1. **设置布局为宽模式**：
   使用 `st.set_page_config(layout="wide")` 将页面布局设为宽模式。

2. **在同一行创建按钮、下拉菜单和复选框**：
   使用 `st.beta_columns` 将按钮、两个下拉菜单和复选框并排显示。

3. **第一个下拉菜单选择比例**：
   提供 "16:9" 和 "9:16" 两个选项，默认选择 "16:9"，并检查当前目录下是否存在同名文件夹。

4. **第二个下拉菜单选择文件夹**：
   第一个选项为 "全部"，其他选项为第一步选择的文件夹中的子文件夹名称。

5. **随机选择并显示图片**：
   根据选择的文件夹随机选择20张图片，并根据比例分列显示（"16:9" 两列，"9:16" 四列）。

6. **复选框控制下载按钮显示**：
   当复选框选中时，在每张图片下方显示下载按钮，点击按钮下载相应图片。

7. **刷新按钮重新随机选择图片**：
   点击刷新按钮时，重新随机选择20张图片并更新显示。

### 代码实现

```python
import streamlit as st
import os
import random
from PIL import Image

# 设置页面布局为宽模式
st.set_page_config(layout="wide")

# 获取当前目录下的文件夹
folders = {"16:9": "16:9", "9:16": "9:16"}
available_folders = {k: v for k, v in folders.items() if os.path.isdir(v)}

# 检查必要文件夹是否存在
if "16:9" not in available_folders and "9:16" not in available_folders:
    st.error("当前目录下没有名为 '16:9' 或 '9:16' 的文件夹。")
    st.stop()

# 创建并排放置的列
col1, col2, col3, col4 = st.beta_columns([1, 2, 2, 1])

# 按钮：刷新图标
with col1:
    refresh = st.button("刷新", key="refresh_button", help="点击刷新图片")

# 第一个下拉菜单：选择比例
with col2:
    aspect_ratio = st.selectbox("选择比例", ["16:9", "9:16"], index=0, key="aspect_ratio")

# 第二个下拉菜单：选择文件夹
with col3:
    # 获取第一步选择的文件夹下的所有子文件夹
    main_folder = folders[aspect_ratio]
    sub_folders = [f for f in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, f))]
    folder_options = ["全部"] + sub_folders
    selected_folder = st.selectbox("选择文件夹", folder_options, index=0, key="selected_folder")

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
    cols = st.beta_columns(2)
elif aspect_ratio == "9:16":
    cols = st.beta_columns(4)
else:
    cols = st.beta_columns(2)  # 默认两列

# 显示图片和下载按钮
for i, img_path in enumerate(selected_images):
    col = cols[i % len(cols)]
    with col:
        img = Image.open(img_path)
        st.image(img, use_column_width=True, caption=os.path.basename(img_path))
        if show_download:
            with open(img_path, "rb") as f:
                btn = st.download_button(
                    label="下载",
                    data=f,
                    file_name=os.path.basename(img_path),
                    mime="image/png"
                )
```

### 代码说明

- **布局设置**：使用 `st.set_page_config(layout="wide")` 设置宽模式，并用 `st.beta_columns` 创建并排组件。
  
- **下拉菜单和复选框**：
  - 第一个下拉菜单选择比例，默认 "16:9"。
  - 第二个下拉菜单根据第一步选择的文件夹动态生成子文件夹选项。
  - 复选框控制下载按钮的显示。

- **图片选择与显示**：
  - 根据选择的文件夹和子文件夹获取图片路径。
  - 随机选择20张图片，并根据比例分列显示。
  - 如果复选框选中，则在图片下方显示下载按钮。

- **刷新功能**：
  - 点击刷新按钮时，重新随机选择20张图片并更新显示。

### 注意事项

- 确保当前目录下有 "16:9" 或 "9:16" 文件夹，并且这些文件夹中包含图片和子文件夹。
- 图片格式支持 `.png`, `.jpg`, `.jpeg`。
- 根据需要调整列数和布局。
