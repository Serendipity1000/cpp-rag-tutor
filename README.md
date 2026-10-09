# 💻 C++ RAG Tutor (基于 RAG 与长效记忆的 C++ 智能私教系统)

本项目是一个专为 **C++ 开发者与学习者**打造的垂直领域 AI 助手。系统结合了 **Retrieval-Augmented Generation (RAG)** 技术与**轻量级长效记忆机制**，通过本地知识库精准解析 C++ 源码与技术文档，旨在辅助进行 C++ 工程源码阅读、概念答疑与高效学习。

---

## 🛠️ 技术栈 (Tech Stack)

- **Core Framework**: LangChain
- **Vector Database**: Chroma (本地向量存储，结合 HuggingFace 嵌入模型 `all-MiniLM-L6-v2`)
- **LLM**: ZhipuAI (GLM-4-flash)
- **Web UI**: Streamlit (支持动态打字机流式输出、侧边栏控制面板)
- **Memory Management**: 自研 Markdown 正则解析器，实现跨重启的上下文无缝衔接

---

## 📂 项目结构 (Project Structure)

```text
cpp-rag-tutor/
├── src/                    # 核心源代码目录
│   ├── app.py              # Streamlit 前端 UI 入口
│   ├── rag_core.py         # RAG 检索流水线与大模型加载逻辑
│   └── utils.py            # 历史记录读写与工具函数
├── archive/                # 早期迭代与历史测试脚本归档
├── cpp_source/             # C++ 源码及垂直知识库素材
├── requirements.txt        # Python 依赖包清单
├── run.bat                 # Windows 一键启动脚本
└── README.md               # 项目说明文档
```

## ⚡ 快速开始 (Quick Start)
1. 克隆仓库
Bash:
git clone [https://github.com/Serendipity1000/cpp-rag-tutor.git](https://github.com/Serendipity1000/cpp-rag-tutor.git)
cd cpp-rag-tutor

2. 安装依赖
建议在 Python 虚拟环境（如 Conda）中安装所需依赖：
Bash:
pip install -r requirements.txt

3. 配置环境变量
在项目根目录下创建一个 .env 文件，填入你的大模型 API Key：
代码段:
ZHIPUAI_API_KEY=你的智谱AI秘钥

4. 启动运行
Windows 用户：直接双击根目录下的 run.bat，或在终端执行：
DOS:
run.bat

通用命令行启动：
Bash:
streamlit run src/app.py

## ✨ 核心特性
垂直领域精准 RAG：隔离大模型幻觉，深度结合本地 C++ 代码库与技术资料进行高精度上下文召回。

轻量级长效记忆：支持跨重启的对话历史回放与 Markdown 持久化记录。

工程化模块解耦：采用标准的 src/ 目录结构与清晰的模块划分，兼具高可维护性与扩展性。