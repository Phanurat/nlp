import pandas as pd
import tkinter as tk
from tkinter import messagebox

# สร้าง DataFrame สำหรับ positive และ negative โพสทิฟ
positive_posts = []
negative_posts = []

def add_post():
    post = text_entry.get("1.0", tk.END).strip()
    sentiment = var_sentiment.get()
    
    if post and sentiment:
        if sentiment == 'positive':
            positive_posts.append(post)
        elif sentiment == 'negative':
            negative_posts.append(post)
        
        text_entry.delete("1.0", tk.END)
        update_display()
    else:
        messagebox.showwarning("Warning", "กรุณากรอกข้อความและเลือก sentiment")

def update_display():
    text_display.config(state=tk.NORMAL)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, "Positive Posts:\n")
    for post in positive_posts:
        text_display.insert(tk.END, f"{post}\n")
    text_display.insert(tk.END, "\nNegative Posts:\n")
    for post in negative_posts:
        text_display.insert(tk.END, f"{post}\n")
    text_display.config(state=tk.DISABLED)

def save_to_csv():
    df_positive = pd.DataFrame({'Posts Facebook': positive_posts, 'sentiment': 'positive'})
    df_negative = pd.DataFrame({'Posts Facebook': negative_posts, 'sentiment': 'negative'})
    df_all = pd.concat([df_positive, df_negative], ignore_index=True)
    df_all.to_csv('posts-quest.csv', index=False)
    messagebox.showinfo("Success", "บันทึกข้อมูลลงไฟล์ posts-quest.csv เรียบร้อยแล้ว")

# ฟังก์ชันคัดลอกและวาง
def copy():
    root.clipboard_clear()
    root.clipboard_append(text_entry.get("sel.first", "sel.last"))

def paste():
    try:
        text_entry.insert(tk.INSERT, root.clipboard_get())
    except tk.TclError:
        pass

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Post Sentiment GUI")

# สร้างเมนู
menu = tk.Menu(root)
root.config(menu=menu)
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# สร้างองค์ประกอบต่าง ๆ ใน GUI
frame = tk.Frame(root)
frame.pack(pady=10)

label_post = tk.Label(frame, text="Post:")
label_post.grid(row=0, column=0, padx=5)

text_entry = tk.Text(frame, width=50, height=10)
text_entry.grid(row=0, column=1, padx=5)

label_sentiment = tk.Label(frame, text="Sentiment:")
label_sentiment.grid(row=1, column=0, padx=5)

var_sentiment = tk.StringVar(value="positive")
radio_positive = tk.Radiobutton(frame, text="Positive", variable=var_sentiment, value="positive")
radio_positive.grid(row=1, column=1, sticky='w', padx=5)
radio_negative = tk.Radiobutton(frame, text="Negative", variable=var_sentiment, value="negative")
radio_negative.grid(row=1, column=1, sticky='e', padx=5)

button_add = tk.Button(frame, text="Add Post", command=add_post)
button_add.grid(row=2, columnspan=2, pady=5)

text_display = tk.Text(root, width=60, height=20, state=tk.DISABLED)
text_display.pack(pady=10)

button_save = tk.Button(root, text="Save to CSV", command=save_to_csv)
button_save.pack(pady=5)

# เริ่มต้นแสดงผล GUI
root.mainloop()
