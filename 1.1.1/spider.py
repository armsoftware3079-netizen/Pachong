# Spider Tool v1.1.1 主程序（多线程 + OCR + Cookie + 主题 + 国际化）
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import shutil
import requests
from bs4 import BeautifulSoup
import queue

try:
    from spider_ocr import recognize_captcha_from_url
except ImportError:
    recognize_captcha_from_url = lambda url: "OCR 模块未安装，请检查 spider_ocr.py"

try:
    import pytesseract
    from PIL import Image
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    ]
    for p in possible_paths:
        if os.path.exists(p):
            pytesseract.pytesseract.tesseract_cmd = p
            break
except ImportError:
    pass

try:
    from spider_ui import create_ui_controls
except ImportError:
    create_ui_controls = lambda root, widgets: tk.Label(root, text="UI 模块未安装")

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
task_queue = queue.Queue()

def fetch_website_code(url, filename="website.html", headers=None):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(res.text)
            return filepath
        return None
    except Exception as e:
        return f"Error: {e}"

def save_uploaded_file(filepath, target_name):
    ext = os.path.splitext(filepath)[1]
    target_path = os.path.join(output_dir, target_name + ext)
    shutil.copy(filepath, target_path)
    return target_path

def handle_task(task_type, data):
    if task_type == "website":
        url, cookie = data
        headers = {"User-Agent": "Mozilla/5.0"}
        if cookie.strip():
            headers["Cookie"] = cookie
        result = fetch_website_code(url, filename="website.html", headers=headers)
        messagebox.showinfo("完成", f"网页已保存: {result}")
    elif task_type in ("software", "miniapp"):
        result = save_uploaded_file(data, "uploaded_" + task_type)
        messagebox.showinfo("完成", f"文件已保存: {result}")

def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        try:
            handle_task(*task)
        except Exception as e:
            messagebox.showerror("错误", str(e))
        task_queue.task_done()

threading.Thread(target=worker, daemon=True).start()

root = tk.Tk()
root.title("Spider Tool v1.1.1")
root.geometry("620x360")
root.configure(bg="#e0f7fa")

widgets = []

url_label = tk.Label(root, text="网址：", bg="#e0f7fa")
url_label.pack()
widgets.append(url_label)
url_entry = tk.Entry(root, width=80)
url_entry.pack(pady=2)
widgets.append(url_entry)

cookie_label = tk.Label(root, text="Cookie：", bg="#e0f7fa")
cookie_label.pack()
widgets.append(cookie_label)
cookie_entry = tk.Entry(root, width=80)
cookie_entry.pack(pady=2)
widgets.append(cookie_entry)

def enqueue_website():
    task_queue.put(("website", (url_entry.get(), cookie_entry.get())))

def enqueue_upload(tag):
    file = filedialog.askopenfilename()
    if file:
        task_queue.put((tag, file))

btn_frame = tk.Frame(root, bg="#e0f7fa")
btn_frame.pack(pady=10)

site_btn = tk.Button(btn_frame, text="爬取网站", command=enqueue_website, width=18)
site_btn.grid(row=0, column=0, padx=5)
widgets.append(site_btn)

soft_btn = tk.Button(btn_frame, text="上传软件", command=lambda: enqueue_upload("software"), width=18)
soft_btn.grid(row=0, column=1, padx=5)
widgets.append(soft_btn)

mini_btn = tk.Button(btn_frame, text="上传小程序", command=lambda: enqueue_upload("miniapp"), width=18)
mini_btn.grid(row=0, column=2, padx=5)
widgets.append(mini_btn)

create_ui_controls(root, widgets)

lang_label = tk.Label(root, text="当前语言：中文（可定制）", bg="#e0f7fa", fg="gray")
lang_label.pack(pady=5)

root.mainloop()
