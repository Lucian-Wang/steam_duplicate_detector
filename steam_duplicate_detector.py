import tkinter as tk
from tkinter import scrolledtext, messagebox

def detect_and_remove_duplicates(input_text):
    lines = input_text.strip().splitlines()
    seen = set()
    unique_lines = []
    duplicates = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped in seen:
            duplicates.append(stripped)
        else:
            seen.add(stripped)
            unique_lines.append(stripped)
    return unique_lines, list(set(duplicates))

def on_check():
    input_text = text_input.get("1.0", tk.END)
    unique_lines, duplicates = detect_and_remove_duplicates(input_text)
    output_text = "\n".join(unique_lines)
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, output_text)
    text_output.config(state=tk.DISABLED)

    if duplicates:
        messagebox.showwarning("检测到重复", f"检测到以下重复账号：\n" + "\n".join(duplicates))
    else:
        messagebox.showinfo("无重复", "未检测到重复账号。")

root = tk.Tk()
root.title("Steam账号去重检测工具")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_input = tk.Label(frame, text="请输入账号列表，每行一个：")
label_input.pack(anchor='w')

text_input = scrolledtext.ScrolledText(frame, width=40, height=10)
text_input.pack()

btn_check = tk.Button(frame, text="检测去重", command=on_check)
btn_check.pack(pady=5)

label_output = tk.Label(frame, text="去重后账号列表：")
label_output.pack(anchor='w')

text_output = scrolledtext.ScrolledText(frame, width=40, height=10, state=tk.DISABLED)
text_output.pack()

# 版权信息
copyright_label = tk.Label(root, text="© 灯火通明（济宁）网络有限公司", fg="gray", font=("Arial", 10))
copyright_label.pack(pady=(5, 10))

root.mainloop()