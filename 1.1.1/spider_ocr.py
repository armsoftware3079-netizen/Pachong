import pytesseract
from PIL import Image
import requests
from io import BytesIO

# 从图片 URL 识别验证码
def recognize_captcha_from_url(image_url):
    try:
        response = requests.get(image_url, timeout=8)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(img)
            return text.strip()
        else:
            return "无法获取图片"
    except Exception as e:
        return f"OCR识别失败: {e}"
