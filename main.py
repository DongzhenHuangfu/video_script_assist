import streamlit as st
import traceback
from utils import generate_script

st.title("🎬 短视频脚本生成工具")

with st.sidebar:
    api_key = st.text_input("Deepseek API密钥：", type="password")
    st.markdown("[获取Deepseek API密钥](https://platform.deepseek.com/api_keys)")
    agree = st.checkbox('DeepThnik(R1)')

subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("⏱️ 请输入视频的大致时长（单位：分钟）", min_value=0.1, step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更具有创造性）", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)
submit = st.button("生成脚本")

if submit and not api_key:
    st.info("Deepseek API密钥未输入")
    st.stop()
if submit and not subject:
    st.info("视频的主题未输入")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()
if submit:
    try:
        with st.spinner("AI正在思考中，请稍等..."):
            deep_think = False
            if agree:
                deep_think = True
            title, script = generate_script(subject, video_length, creativity, deep_think, api_key)
        st.success("视频脚本已生成！")
        st.subheader("🔥 标题：")
        st.write(title)
        st.subheader("📝 视频脚本：")
        st.write(script)
        with st.expander("搜索结果 👀"):
            st.info("暂不支持")
    except Exception as e:
        traceback.print_exc()
        st.error("Deepseek又宕机了，请稍后再试~")
        st.stop()