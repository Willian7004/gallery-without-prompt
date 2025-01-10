gallery-without-prompt

本项目展示的图片生成流程为：使用Flux.1 dev生成720p图片再使用Flux.1 schnell图生图生成1440p图片，在生成时不填写提示词。这样生成效果优于直接使用Flux.1 schnell，分辨率优于直接使用Flux.1 dev。图片有16：9和9：16两种宽高比，选择宽高比后随机显示图片。

当前为第二版，由于第一版因风格不明确导致出片率较低，本版本改为使用3种风格提示词分别生成。照片风格主要排除了光照或材质有问题的图片。动漫风格相比完整提示词，生成的图片风格接近手绘。油画风格生成的实际风格有一部分是旧模型的风格或纹理异常，也排除了这一部分。总体质量和出片率明显优于第一版。可以在release中找到历史版本。

本项目逻辑部分使用LLM辅助生成，对话记录位于streamlit_app.md。第二版的逻辑功能也进行了调整，加大了页面宽度，改为双列显示16：9图片，分四列显示9：16图片。

本项目已部署到Streamlit Cloud，域名为https://william7004-gallery-without-prompt.streamlit.app

本地部署流程

建议使用Python=3.10环境

1.安装依赖
```bash
pip install -r requirements.txt
```
2.运行应用
```bash
streamlit run streamlit_app.py
```

