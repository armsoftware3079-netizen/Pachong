# 🕷️ Python Web Crawler Tool (Spider Tool)

A graphical, multi-purpose tool for extracting source code from websites, software, and mini programs.

---

## 📦 Features

✅ Supports three types of input:
- 🌐 Website source code (including complex sites like `.cn` domains)
- 💾 Local software source extraction (`.exe`, `.cpp`, etc.)
- 📱 Mini program package resource extraction (automatically zipped)

✅ Output:
- Automatically determines file type and extension (`.html`, `.cpp`, `.zip`, etc.)
- Multi-file output will be zipped automatically

✅ User Interface:
- GUI-based, no command line needed
- One-click buttons: "Crawl Website", "Upload Software", "Upload Mini Program"

✅ Technology Stack:
- `requests`, `beautifulsoup4`, `scrapy`, `selenium`
- Dynamic rendering support, anti-crawl simulation, proxy pool available in advanced mode

---

## 🚀 Quick Start

### ▶️ Option 1: Run from Source

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the crawler tool:

   ```bash
   python spider.py
   ```

---

### 💡 Option 2: Use Installer

1. Run `spider.py`.
2. Please your computer has Python.
3. Run Use!

---

## 📁 Project Structure

```bash
I:\python-crawler\
├── spider.py             # Main script (GUI + logic)
├── requirements.txt      # Python dependencies
├── installer.nsi         # NSIS script for creating installer
├── dist/spider.exe       # Compiled executable (optional)
├── output/               # Directory for saved results
└── README.md             # This documentation
```

---

## ⚙️ System Requirements

| Item            | Minimum Requirement         |
|----------------|-----------------------------|
| Operating System | Windows 10 or later        |
| Python Version  | Python 3.8+                 |
| Browser Driver  | ChromeDriver (for Selenium) |
| Internet Access | Required for web crawling   |

---

## 🧪 Required Python Libraries

```bash
pip install requests beautifulsoup4 selenium scrapy
```

> Note: For `Selenium`, make sure you install the matching [ChromeDriver](https://chromedriver.chromium.org/downloads) version.

---

## ⚠️ Usage Disclaimer

- Do **NOT** use this tool for illegal purposes.
- This tool is only for:
  - Education
  - Technical validation
  - Teaching demos
  - Research
- Users are solely responsible for any legal consequences.
- Respect target websites' terms of use and robots.txt rules.

---

## 🛠️ Developer Notes

- If `pyinstaller` is not recognized, use:

  ```bash
  python -m PyInstaller --onefile --windowed spider.py
  ```

- To build an installer, use NSIS and compile the `installer.nsi` script.

---

## 🗂️ Changelog

### v1.0 Initial Release
- GUI with Website / Software / Mini Program crawling
- Auto file-type recognition and saving
- Dynamic web crawling support
- NSIS installer ready

---

## 📮 Contact

For feedback or issues, contact the developer or submit an issue on the project page.

> Thank you for using the Python Spider Tool! 🙌
