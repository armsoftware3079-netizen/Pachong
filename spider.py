import requests
import zipfile
import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox


# 获取网页内容
def fetch_website(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败会抛出异常
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        return True
    except requests.exceptions.RequestException as e:
        return f"请求失败: {e}"

# 判断文件后缀名并保存源代码文件
def save_source_code(file_path, save_path):
    try:
        # 获取文件的后缀名
        file_extension = os.path.splitext(file_path)[1].lower()

        # 读取源代码并保存
        with open(file_path, 'r') as source_file:
            code_content = source_file.read()

        # 根据文件后缀名保存不同类型的源代码
        with open(save_path, 'w') as save_file:
            save_file.write(code_content)
        return save_path
    except Exception as e:
        return f"文件保存失败: {e}"

# 解压文件（.zip）
def extract_zip(file_path, destination_folder):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
        os.remove(file_path)  # 删除 zip 文件
        return destination_folder
    except zipfile.BadZipFile as e:
        return f"解压失败: {e}"

# GUI 窗口
class UniversalSpiderGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("通用爬虫工具")
        self.window.geometry("600x400")

        # 输入框
        self.label_url = Label(self.window, text="请输入网址或文件/小程序链接：")
        self.label_url.pack(pady=10)

        self.entry_url = Entry(self.window, width=50)
        self.entry_url.pack(pady=5)

        # 爬取网站按钮
        self.fetch_button = Button(self.window, text="爬取网站", command=self.fetch_website)
        self.fetch_button.pack(pady=10)

        # 上传软件按钮
        self.upload_software_button = Button(self.window, text="上传源代码", command=self.upload_software)
        self.upload_software_button.pack(pady=10)

        # 上传小程序按钮
        self.upload_mini_program_button = Button(self.window, text="上传小程序", command=self.upload_mini_program)
        self.upload_mini_program_button.pack(pady=10)

    # 爬取网站
    def fetch_website(self):
        url = self.entry_url.get()
        if not url:
            messagebox.showerror("错误", "请提供网址！")
            return
        print(f"爬取网站：{url}")
        page_source = fetch_website(url, "webpage_source.html")
        if page_source is True:
            messagebox.showinfo("成功", "网页源代码已保存为 webpage_source.html")
        else:
            messagebox.showerror("错误", page_source)

    # 上传软件源代码
    def upload_software(self):
        file_path = filedialog.askopenfilename(title="选择源代码文件", filetypes=[("Source Code Files", "*.cpp;*.h;*.html;*.js;*.css;*.txt")])
        if not file_path:
            messagebox.showerror("错误", "未选择文件！")
            return
        
        # 判断文件的保存路径
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension in ['.cpp', '.h']:
            save_path = os.path.join(os.getcwd(), os.path.basename(file_path))  # C++ 代码文件
        elif file_extension in ['.html', '.htm']:
            save_path = os.path.join(os.getcwd(), os.path.basename(file_path))  # 网页文件
        else:
            save_path = os.path.join(os.getcwd(), f"source_code{file_extension}")  # 其他文件类型

        print(f"保存源代码：{file_path}")
        saved_file = save_source_code(file_path, save_path)
        if saved_file:
            messagebox.showinfo("成功", f"源代码已保存为：{saved_file}")
        else:
            messagebox.showerror("失败", "文件保存失败！")

    # 上传小程序
    def upload_mini_program(self):
        file_path = filedialog.askopenfilename(title="选择小程序", filetypes=[("Zip files", "*.zip")])
        if not file_path:
            messagebox.showerror("错误", "未选择文件！")
            return
        print(f"解压小程序：{file_path}")
        folder = extract_zip(file_path, os.getcwd())
        if folder:
            messagebox.showinfo("成功", f"小程序已解压到：{folder}")
        else:
            messagebox.showerror("失败", "小程序解压失败！")

    # 启动窗口
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    spider_gui = UniversalSpiderGUI()
    spider_gui.run()
