# 🕷️ Spider Tool v1.0.1

**多功能图形化爬虫工具**  
支持网页、软件和小程序源代码提取，并具备智能识别、日志记录、美化界面及自动保存功能。

---

## 📦 目录结构

```
python-crawler/
├── spider.py              # 主程序 (GUI + 智能爬虫 + 日志)
├── requirements.txt       # 所需依赖库
├── installer.nsi          # NSIS 安装脚本
├── dist/spider.exe        # 可执行文件（可选）
├── output/                # 爬取输出目录
├── logs/spider.log        # 日志文件
└── README.md              # 本文档
```

---

## ✨ 功能亮点

### 🎨 图形化界面（Tkinter 美化）
- 扁平化设计、彩色按钮风格
- 状态栏实时提示
- 界面简洁明快、支持中文字体

### 🌐 智能网页爬取
- 优先尝试静态爬虫（requests + bs4）
- 若失败，自动切换动态爬虫（Selenium）
- 可爬取 `GitHub.com`, `ChatGPT.com`, `.cn` 网站等复杂目标

### 💻 软件/小程序源代码上传识别
- 识别上传文件后缀
- 自动保存为 `.cpp`, `.py`, `.zip` 等格式
- 文件输出路径统一保存在 `output/`

### 📜 日志记录功能
- 操作日志自动写入 `logs/spider.log`
- 包含请求成功/失败、错误堆栈等内容
- 便于长期维护和排错

---

## 🚀 使用说明

### ✅ 安装依赖

```bash
pip install -r requirements.txt
```

或使用虚拟环境：

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### ▶️ 运行程序

```bash
python spider.py
```

> 推荐使用 Python 3.9+，需预装 Chrome 浏览器与对应版本 ChromeDriver。

---

## 🔐 安全说明

- 工具仅用于**合法授权的内容爬取**
- 请勿用于侵犯知识产权的网站或平台
- 若目标站点使用防爬措施（如 Cloudflare），需配置代理或模拟登录

---

## 📜 更新日志 v1.0.1

- [x] UI 美化，增加图标、颜色、状态提示
- [x] 智能判断网页爬虫策略（静态 / 动态）
- [x] 支持上传并保存源码、自动识别格式
- [x] 日志记录完善，错误跟踪清晰
- [x] 所有输出统一保存至 output/ 文件夹

---

## 📦 安装包生成（可选）

1. 安装 pyinstaller：

```bash
pip install pyinstaller
pyinstaller --onefile --windowed spider.py
```

2. 编写并使用 NSIS 安装脚本（installer.nsi）

3. 欢迎大家把自己修改的文件所生成的安装包投稿，谢谢！

---

## 📬 联系作者

如需自定义版本、添加功能或商业授权，请联系：

📧 Email: [Armsoftware3079@gmail.com](mailto:Armsoftware3079@gmail.com)

---

© 2025 Spider Tool 开发组 | 仅供学习与研究使用
