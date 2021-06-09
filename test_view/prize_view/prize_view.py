# -*- encoding=utf8 -*-

__author__ = "zhaobl01"

import re

from airtest.core.api import *
from airtest.aircv import *
from airtest.cli.parser import cli_setup

from common import common
from test_view.login_view.login_view import LoginView
from config.settings import params

if not cli_setup():
    project_root = sys.path[1].replace("\\", "/")
    auto_setup(__file__, logdir=True, devices=["Android:///", ], project_root=project_root)

PACKAGE_NAME = params["package_name"]


class Prize:
    """
    抽奖转盘领取奖励后，验证现金是否领取成功
    """
    def __init__(self):
        self.project_path = params["project_root_path"]

    def get_cash(self):
        """
        获取现金数
        """
        try:
            center = wait(
                Template(r"../../imgs/icon/cash_icon.png", threshold=0.6999999999999997,
                         target_pos=1, record_pos=(-0.349, -0.224),
                         resolution=(2232, 1080), ), timeout=20, interval=3
            )
        except TargetNotFoundError:
            print("未找现金")
        x = center[0]
        y = center[1]

        auto_setup(__file__)
        screen = G.DEVICE.snapshot()

        # 局部截图
        local = aircv.crop_image(screen, (x, y, x + 200, y + 60))
        snapshot(filename='get_cash.png')

        # 保存局部截图到测试结果集文件夹中
        pil_image = cv2_2_pil(local)
        pil_image.save("../../test_result_imgs/get_cash.png", quality=99, optimize=True)
        img_path = self.project_path + '/test_result_imgs/get_cash.png'
        cash_result = common.img_ocr(img_path)
        cash_result = re.findall("(\d+)", cash_result)
        cash_result = "".join(cash_result)

        sleep(5)
        clear_app(PACKAGE_NAME)
        stop_app(PACKAGE_NAME)

        return cash_result


if __name__ == '__main__':
    login = LoginView()
    login.login_as_guest()
    login.close_tap()
    logined = login.check_logined()

    if logined:
        print("登陆成功")
        p = Prize()
        cash = p.get_cash()
        print("现金数:", cash)
    else:
        print("登陆未成功")
