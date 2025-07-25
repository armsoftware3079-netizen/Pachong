import tkinter as tk
from tkinter import ttk

def create_ui_controls(root, widgets):
    style_var = tk.StringVar(value="Sky")
    font_var = tk.StringVar(value="Microsoft YaHei")

    def apply_ui():
        selected_font = font_var.get()
        for w in widgets:
            try:
                w.configure(font=(selected_font, 10))
            except:
                pass
        root.update()

    style_frame = tk.LabelFrame(root, text="界面设置", bg="#e0f7fa")
    style_frame.pack(pady=5)

    tk.Label(style_frame, text="主题风格：", bg="#e0f7fa").grid(row=0, column=0)
    style_dropdown = ttk.Combobox(style_frame, textvariable=style_var, values=["Sky", "Dark", "Classic"], width=12)
    style_dropdown.grid(row=0, column=1)

    tk.Label(style_frame, text="字体：", bg="#e0f7fa").grid(row=0, column=2)
    font_dropdown = ttk.Combobox(style_frame, textvariable=font_var, values=["Microsoft YaHei", "Arial", "Courier New", "SimSun"], width=15)
    font_dropdown.grid(row=0, column=3)

    apply_button = tk.Button(style_frame, text="应用", command=apply_ui)
    apply_button.grid(row=0, column=4, padx=10)
