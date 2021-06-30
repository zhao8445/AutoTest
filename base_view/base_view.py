from PIL import Image
import logging

from airtest.core.api import *
from airtest.aircv import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report

from config.settings import params

PROJECT_ROOT_PATH = params["project_root_path"]

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
        fmt = "[%(asctime)s] - %(filename)s - line:%(lineno)2d - %(levelname)s: %(message)s"
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
        :return:
        """
        auto_setup(__file__)
        screen = G.DEVICE.snapshot(quality=99)

        # 局部截图
        local = aircv.crop_image(screen, (x_start, y_start, x_end, y_end))

        # 保存局部截图到测试结果集文件夹中
        pil_image = cv2_2_pil(local).convert()
        save_path = PROJECT_ROOT_PATH + '/test_result_imgs/' + filename
        pil_image.save(save_path, quality=99, optimize=True)
        logger.info("局部截图 %s" % filename)

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
            # logger.error("关闭按钮未找到")


bv = BaseView()
logger = bv.setLog()


