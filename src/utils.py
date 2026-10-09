import os
import re

def load_recent_history_from_md(file_path="chat_history.md", max_turns=5):
    chat_history = []
    ui_messages = []
    
    if not os.path.exists(file_path):
        return chat_history, ui_messages

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r"### Q: (.*?)\n\n\*\*A:\*\*\n(.*?)\n\n---"
        matches = re.findall(pattern, content, re.DOTALL)

        if matches:
            recent_matches = matches[-max_turns:]
            for q, a in recent_matches:
                chat_history.append(("human", q.strip()))
                chat_history.append(("ai", a.strip()))
                ui_messages.append({"role": "user", "content": q.strip()})
                ui_messages.append({"role": "assistant", "content": a.strip()})
    except Exception as e:
        print(f"加载历史记录失败: {e}")

    return chat_history, ui_messages

def save_turn_to_md(question, answer, file_path="chat_history.md"):
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"### Q: {question}\n\n")
            f.write(f"**A:**\n{answer}\n\n")
            f.write("---\n\n")
    except Exception as e:
        print(f"保存历史记录失败: {e}")