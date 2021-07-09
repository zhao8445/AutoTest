import logging

from airtest.core.api import *
from airtest.aircv import *
from airtest.cli.parser import cli_setup

from config.settings import params
from utils import baidu_ocr
from utils.baidu_ocr import img_ocr_list

PROJECT_ROOT_PATH = params["project_root_path"]
IMGS_PATH = PROJECT_ROOT_PATH + "/imgs/icon/"

if not cli_setup():
    project_root = sys.path[1].replace("\\", "/")
    auto_setup(__file__, logdir=True, devices=["Android:///", ], project_root=project_root)


class BaseView:
    def setLog(self):
        """
        写入日志
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.DEBUG)
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        log_path = PROJECT_ROOT_PATH + '/logs/'
        if not os.path.exists((log_path)):
            os.mkdir(log_path)
        handler = logging.FileHandler(log_path + now + "_log.txt")
        handler.setLevel(logging.DEBUG)
        # fmt = "[%(asctime)s] - %(filename)20s - line:%(lineno)2d - %(levelname)s: %(message)s"
        fmt = "[%(asctime)s] - %(levelname)5s: %(message)s"
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def partial_screenshot(self, x_start, y_start, x_end, y_end, filename):
        """
        局部截图
        :param x_start: 起始x坐标
        :param y_start: 起始y坐标
        :param x_end: 终止x坐标
        :param y_end: 终止y坐标
        :param filename: 保存的文件名
        :return: 图片路径
        """
        auto_setup(__file__)
        screen = G.DEVICE.snapshot(quality=99)

        # 局部截图
        local = aircv.crop_image(screen, (x_start, y_start, x_end, y_end))

        # 保存局部截图到测试结果集文件夹中
        pil_image = cv2_2_pil(local).convert()
        save_path = PROJECT_ROOT_PATH + '/test_result_imgs/' + filename
        pil_image.save(save_path, quality=99, optimize=True)

        return save_path

    def click_close_btn(self):
        """
        点击关闭按钮
        :return:
        """
        try:
            position = wait(
                Template(
                    PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", threshold=0.90, record_pos=(0.382, -0.217),
                    resolution=(2232, 1080)
                ), timeout=2, interval=1)
            while position:
                touch(position)
                sleep(2)
                position = wait(
                    Template(
                        PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", threshold=0.90,
                        record_pos=(0.382, -0.217), resolution=(2232, 1080)
                    ), timeout=2, interval=1
                )
        except TargetNotFoundError:
            pass

    def read_txt(self, txt_path):
        """
        阅读打开txt文件
        :param txt_path: txt文件路径
        :return: 文件内容结果集
        """
        res = []
        with open(txt_path, encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            res.append(line.strip('\n'))
        return res

    def get_ocr_result(self, start_position, end_position, filename):
        """
        获取图片识别结果
        :param start_position: 图片起始坐标
        :param end_position: 图片终止坐标
        :param filename: 文件名
        :return: 识别结果
        """
        screenshot_path = bv.partial_screenshot(
            start_position[0], start_position[1], end_position[0], end_position[1], filename
        )
        ocr_result = img_ocr_list(screenshot_path)
        return ocr_result

    def get_cash(self):
        """
        获取现金数
        """
        cash_result = 0
        try:
            center = wait(
                Template(IMGS_PATH + r"cash_icon.png", threshold=0.6999999999999997, target_pos=1,
                         record_pos=(-0.349, -0.224), resolution=(2232, 1080), ), timeout=5, interval=1
            )
            x_start = center[0]
            y_start = center[1]

            img_path = bv.partial_screenshot(x_start+40, y_start, x_start+200, y_start+40, 'get_cash.png')
            cash_result = baidu_ocr.img_ocr(img_path)
            cash_result = "".join(list(filter(str.isdigit, cash_result)))
        except TargetNotFoundError:
            logger.error("未找到现金ICON")

        return cash_result


bv = BaseView()
logger = bv.setLog()

