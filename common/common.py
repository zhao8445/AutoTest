from PIL import Image
from pytesseract import *
from airtest.core.api import *
from airtest.aircv import *

from config.settings import params

PROJECT_ROOT_PATH = params["project_root_path"]


def img_ocr(img_path):
    """
    识别图像上的文字
    :param img_path: 图片路径
    :return: 识别结果
    """
    pic = Image.open(img_path)
    pic_gray = pic.convert("L")
    # pic_gray.show()
    text = image_to_string(pic_gray)
    return text

def partial_screenshot(x_start, y_start, x_end, y_end, filename):
    """
    局部截图
    :param x_start: 起始x坐标
    :param y_start: 起始y坐标
    :param x_end: 终止x坐标
    :param y_end: 终止y坐标
    :param filename: 保存的文件名
    :return:
    """
    auto_setup(__file__)
    screen = G.DEVICE.snapshot()

    # 局部截图
    local = aircv.crop_image(screen, (x_start, y_start, x_end, y_end))
    # snapshot(filename=filename)

    # 保存局部截图到测试结果集文件夹中
    pil_image = cv2_2_pil(local)
    save_path = PROJECT_ROOT_PATH + '/test_result_imgs/' + filename
    pil_image.save(save_path, quality=99, optimize=True)

    return save_path

def click_close_btn():
    """
    点击关闭按钮
    :return:
    """
    try:
        position = wait(Template(r"../../imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
                                 resolution=(2232, 1080)), timeout=5, interval=1)
        while position:
            touch(position)
            position = wait(Template(r"../../imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
                                     resolution=(2232, 1080)), timeout=5, interval=1)
    except TargetNotFoundError:
        print("Close Button Not Found")
        pass

if __name__ == "__main__":
    img_path = "C:/Users/zhaobl01/Desktop/AuguPokerAirTest/log/1623122970788.jpg"
    img_ocr(img_path)
