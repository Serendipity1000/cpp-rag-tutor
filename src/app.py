import os
import warnings
from dotenv import load_dotenv
import streamlit as st

from utils import load_recent_history_from_md, save_turn_to_md
from rag_core import init_rag_chain # 导入了 rag_core.py 里的函数 ──> init_rag_chain

# 屏蔽警告
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*HMAC key is 16 bytes long.*")

load_dotenv()

# 设置页面配置
st.set_page_config(page_title="C++ 线程池 AI 私教", page_icon="💻", layout="centered")

# 使用缓存装饰器加载引擎，避免重复开销
@st.cache_resource
def cached_init_rag_chain():
    return init_rag_chain()

rag_chain = cached_init_rag_chain()

# --- 侧边栏设计 (控制面板) ---
with st.sidebar:
    st.header("⚙️ 控制面板")
    st.markdown("---")
    
    # 清空对话按钮
    if st.button("🗑️ 清空当前对话与历史", type="primary"):
        st.session_state.chat_history = []
        st.session_state.messages = []
        if os.path.exists("chat_history.md"):
            os.remove("chat_history.md")
        st.success("历史记录已清空！")
        st.rerun()
        
    st.markdown("---")
    st.markdown("### 📌 项目简介")
    st.markdown("基于 **LangChain + Chroma + Streamlit** 的 C++ 多线程垂直领域 RAG 智能私教系统。")

# 主界面标题
st.title("💻 C++ 线程池智能私教助手")
st.caption("基于 RAG 检索增强与跨重启长效记忆的学习伴侣")

# 初始化 Session State
if "messages" not in st.session_state:
    initial_history, initial_ui = load_recent_history_from_md("chat_history.md", max_turns=5)
    st.session_state.chat_history = initial_history
    st.session_state.messages = initial_ui

# 渲染网页气泡
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 处理用户输入
if prompt_input := st.chat_input("向你的 C++ 私教提问吧..."):
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_answer = ""
        
        input_data = {
            "input": prompt_input,
            "chat_history": st.session_state.chat_history
        }

        # 流式打字机输出
        for chunk in rag_chain.stream(input_data):
            if "answer" in chunk:
                piece = chunk["answer"]
                full_answer += piece
                message_placeholder.markdown(full_answer + "▌")
        
        message_placeholder.markdown(full_answer)

    # 更新内存状态
    st.session_state.chat_history.append(("human", prompt_input))
    st.session_state.chat_history.append(("ai", full_answer))
    st.session_state.messages.append({"role": "assistant", "content": full_answer})

    # 同步写入长期记忆 Markdown
    save_turn_to_md(prompt_input, full_answer, "chat_history.md")

# rag_chain = init_rag_chain()  # 实际上执行的是 rag_core.py 里的代码