# -*- encoding=utf8 -*-

__author__ = "zhaobl01"

from airtest.core.api import *
from airtest.aircv import *
from airtest.cli.parser import cli_setup

from config.settings import params

if not cli_setup():
    project_root = sys.path[1].replace("\\", "/")
    auto_setup(__file__, logdir=True, devices=["Android:///", ], project_root=project_root)

PACKAGE_NAME = params["package_name"]


class LoginView:
    def __init__(self):
        # 启动APP
        start_app(PACKAGE_NAME)

    def login_as_guest(self):
        """
        访客登陆
        :return:
        """
        try:
            wait(Template(r"../../imgs/login/continue_as_guest.png", record_pos=(0.002, 0.196), resolution=(1280, 800)),
                 timeout=15, interval=5)
            touch(
                Template(r"../../imgs/login/continue_as_guest.png", record_pos=(0.005, 0.193), resolution=(1280, 800)))
        except TargetNotFoundError:
            print("未找到登陆按钮")

    def close_tap(self):
        """
        关闭签到登陆等tab页
        :return:
        """
        try:
            position = wait(Template(r"../../imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
                                     resolution=(2232, 1080)), timeout=10, interval=5)
            while position:
                touch(position)
                position = wait(Template(r"../../imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
                                         resolution=(2232, 1080)), timeout=10, interval=5)
        except TargetNotFoundError:
            print("未找到TAg关闭按钮")
            pass

    def check_logined(self):
        try:
            assert_exists(
                Template(r"../../imgs/login/play_now_btn.png", record_pos=(-0.001, 0.205), resolution=(2232, 1080)),
                "通过PLAY_NOW按钮判断是否登陆")
            return True
        except AssertionError:
            return False

#
# if __name__ == '__main__':
#     l = LoginView()
#     l.login_as_guest()
