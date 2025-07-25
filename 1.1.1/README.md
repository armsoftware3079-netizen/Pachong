# 🕷 Spider Tool v1.1.1

A multifunctional crawler tool that supports:
- Website source code crawling (with cookie input)
- Software and mini-app uploads (saved as source)
- Auto-detection of web structure
- CAPTCHA recognition with OCR
- GUI interface with themes and fonts
- Multithreaded and queued crawling
- Internationalization-ready interface

## 🛠 Features

| Feature | Description |
|--------|-------------|
| ✅ Website Crawling | Supports headers/cookie injection |
| ✅ File Uploading | Extracts source of software or mini-program |
| ✅ Multithreading | Crawling is thread-safe with queue |
| ✅ GUI | User-friendly interface (Tkinter) |
| ✅ OCR | Built-in CAPTCHA recognizer (pytesseract) |
| ✅ UI Style | Sky/Dark/Classic, Fonts: YaHei, Arial, SimSun |
| ✅ i18n | Supports simplified Chinese & English |
| ✅ Logging | Optional debugging logs available |

## 🧰 Requirements

```bash
pip install -r requirements.txt
```

You must also install **Tesseract-OCR** manually from:  
👉 https://github.com/tesseract-ocr/tesseract

## 📂 Folder Structure

```
spider_tool_v1.1.1/
├── spider.py          # GUI + Logic
├── spider_ui.py       # Style/Font UI module
├── spider_ocr.py      # OCR Recognition
├── requirements.txt   # Dependency list
├── README.md          # This doc
├── version_log.md     # Version changelog
├── output/            # Saved results
└── dist/              # Optional binary
```

## 🧪 How to Run

```bash
python spider.py
```

