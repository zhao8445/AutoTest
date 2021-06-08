from PIL import Image
from pytesseract import *

def img_ocr(img_path):
    """
    :param img_path: 图片路径
    :return: 识别结果
    """
    pic = Image.open(img_path)
    pic_gray = pic.convert("L")
    # pic_gray.show()
    text = image_to_string(pic_gray)
    return text

if __name__ == "__main__":
    img_path = "C:/Users/zhaobl01/Desktop/AuguPokerAirTest/log/1623122970788.jpg"
    img_ocr(img_path)
