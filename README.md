# 💻 C++ Thread Pool AI Tutor (基于 RAG 与长效记忆的智能私教系统)

本项目是一个面向 C++ 多线程与并发编程领域的垂直应用 AI 助手。系统结合了 **Retrieval-Augmented Generation (RAG)** 技术与**轻量级持久化长效记忆机制**，并使用 **Streamlit** 搭建了现代化的响应式 Web 交互界面。

---

## 🚀 核心架构与技术栈

- **Core Framework**: LangChain
- **Vector Database**: Chroma (本地向量存储，结合 HuggingFace 嵌入模型 `all-MiniLM-L6-v2`)
- **LLM**: ZhipuAI (GLM-4-flash)
- **Web UI**: Streamlit (支持动态打字机流式输出、侧边栏控制面板)
- **Memory Management**: 自研 Markdown 正则解析器，实现跨重启的上下文无缝衔接

---

## 🛠️ 项目结构

```text
├── app.py              # Streamlit 网页端主入口与交互逻辑
├── rag_core.py         # RAG 检索流水线与大模型初始化
├── utils.py            # 本地 Markdown 记忆读写与正则解析模块
├── chat_history.md     # 跨重启持久化长效记忆存储文件
├── requirements.txt    # 项目依赖包
└── .env                # 环境变量配置 (API 密钥保护)