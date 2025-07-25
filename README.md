# 🕷️ Spider Tool v1.1.1

**Spider Tool** 是一款跨平台的图形化爬虫工具，适用于网站源码获取、软件和小程序源码提取，具备智能化结构解析、OCR验证码识别、多线程与队列调度功能，并支持自定义界面风格与字体。

---

## ✨ 主要特性

| 功能 | 描述 |
|------|------|
| 🌐 网页爬取 | 支持静态网页和结构自动分析，支持输入 Cookie |
| 📦 软件/小程序上传 | 自动识别源代码并打包输出 |
| 🧠 多线程 + 队列爬虫 | 高效稳定的并发任务管理 |
| 🧩 CAPTCHA 识别 | 集成 OCR 模块 `pytesseract` |
| 🎨 界面可定制 | 提供多种 UI 风格与字体切换（实时生效） |
| 🌍 国际化支持 | 默认中文，可扩展英文界面（预留） |
| 📜 日志记录 | 控制台输出调试日志，可选切换 |
| 📁 输出管理 | 所有爬取结果自动保存至 `output/` 文件夹 |

---

## 📁 项目结构

```
spider_tool_v1.1.1/
├── spider.py          # 主程序 (GUI + 核心逻辑)
├── spider_ui.py       # UI 风格与字体设置模块
├── spider_ocr.py      # OCR 验证码识别模块
├── requirements.txt   # Python依赖包
├── README.md          # 本说明文件
├── version_log.md     # 版本更新日志
├── installer.nsi      # NSIS 安装脚本（可选）
├── dist/spider.exe    # 可选打包后的可执行文件
└── output/            # 爬取结果输出目录
```

---

## 🧰 安装依赖

```bash
pip install -r requirements.txt
```

> ⚠️ 本工具需要 Tesseract OCR，请手动下载安装：
> https://github.com/tesseract-ocr/tesseract  
> 并添加到系统环境变量中。

---

## 🚀 使用方法

```bash
python spider.py
```

或在 Windows 上双击运行 `spider.exe`（若已打包）。

---

## 📦 打包成安装程序（可选）

使用 `NSIS` 工具打开 `installer.nsi` 脚本即可生成 `.exe` 安装包。

---

## 📘 许可证

本项目遵循 MIT License 开源协议，欢迎自由使用与修改。

---

© 2025 SpiderSoft | Version: **v1.1.1**
