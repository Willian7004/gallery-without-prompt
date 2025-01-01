gallery-without-prompt

本项目展示的图片生成流程为：使用Flux.1 dev生成720p图片再使用Flux.1 schnell图生图生成1440p图片，在生成时不填写提示词。这样生成效果优于直接使用Flux.1 schnell，分辨率优于直接使用Flux.1 dev。图片有16：9和9：16两种宽高比，选择宽高比后随机显示图片。
本项目每次更新会替换图片，在release中查看历史版本。
本项目逻辑部分使用LLM辅助生成，对话记录位于streamlit_app.txt
本项目已部署到Streamlit Cloud，域名为https://william7004-gallery-without-prompt.streamlit.app

本地部署流程

建议使用Python=3.10环境

1.安装依赖
pip install -r requirements.txt

2.运行应用

streamlit run streamlit_app.py