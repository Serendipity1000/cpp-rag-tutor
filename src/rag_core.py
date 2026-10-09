import os

# --- 关键修复：开启 Hugging Face 国内镜像加速，解决连接超时问题 ---
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatZhipuAI

def init_rag_chain():
    # 使用国内镜像后，这里下载或检查模型就会秒通
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

    llm = ChatZhipuAI(model="glm-4-flash", temperature=0.1)

    system_prompt = (
        "你是一个精通 C++ 和多线程编程的 AI 专家助手。\n"
        "请根据下面提供的真实 C++ 源码片段，准确、专业地回答用户的问题。\n"
        "如果源码中没有相关信息，请直接说明，不要凭空猜测。\n\n"
        "相关代码上下文：\n"
        "{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    return rag_chain