# -*- encoding=utf8 -*-

__author__ = "zhaobl01"

import re

from airtest.cli.parser import cli_setup

from common.common import *
from test_view.login_view.login_view import LoginView
from config.settings import params

if not cli_setup():
    project_root = sys.path[1].replace("\\", "/")
    auto_setup(__file__, logdir=False, devices=["Android:///", ], project_root=project_root)

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
                         resolution=(2232, 1080), ), timeout=5, interval=1
            )
            x = center[0]
            y = center[1]

            img_path = partial_screenshot(x, y, x + 200, y + 50, "get_cash.png")

            cash_result = img_ocr(img_path)
            cash_result = re.findall("(\d+)", cash_result)
            cash_result = "".join(cash_result)
        except TargetNotFoundError:
            print("未找到现金")

        return cash_result

    def draw_span(self):
        """
        转盘抽奖
        :return:
        """
        try:
            spin_icon_position = wait(Template(r"./imgs/spin_icon.png", record_pos=(0.173, -0.209), resolution=(2232, 1080)),
                 timeout=5, interval=1)
            touch(spin_icon_position)
        except TargetNotFoundError:
            print("SPIN icon Not Found")
            pass
        try:
            spin_btn_position = wait(Template(r"./imgs/spin_btn.png", record_pos=(0.001, -0.006), resolution=(2232, 1080)),
                 timeout=5, interval=1)
            touch(spin_btn_position)
        except TargetNotFoundError:
            print("SPIN Button Not Found")
            pass
        try:
            collect_btn_postion = wait(
                Template(r"./imgs/collect_btn.png", target_pos=1, record_pos=(-0.004, 0.093), resolution=(2232, 1080)),
                timeout=5, interval=1,
            )
            x_start, y_start = collect_btn_postion[0], collect_btn_postion[1]
            img_path = partial_screenshot(x_start, y_start, x_start + 400, y_start - 100, "./imgs/collected_chips.png")
            touch((x_start+200, y_start+50))
            cash = img_ocr(img_path)
            reward_cash = int("".join(re.findall("(\d+)K", cash))) * 1000
            return reward_cash
        except TargetNotFoundError:
            print("Collect Button Not Found")
        click_close_btn()
        return 0


if __name__ == '__main__':
    login = LoginView()
    login.login_as_guest()
    login.close_tap()
    logined = login.check_logined()

    if logined:
        print("登陆成功")
        p = Prize()
        before_collected_cash = p.get_cash()
        reward_cash = p.draw_span()
        after_colleted_cash = p.get_cash()
        collected_cash = int(after_colleted_cash) - int(before_collected_cash)
        print("领取前的筹码数", before_collected_cash)
        print("领取后的筹码数", after_colleted_cash)
        print("奖励的筹码数为", reward_cash)
        print("领取的筹码数为", collected_cash)
    else:
        print("登陆未成功")
    login.logout()