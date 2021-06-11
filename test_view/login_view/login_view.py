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
            position = wait(Template(r"../../imgs/login/continue_as_guest.png", record_pos=(0.002, 0.196), resolution=(1280, 800)),
                 timeout=20, interval=1)
            touch(position)
        except TargetNotFoundError:
            print("Login as Guest Button Not Found")

    def close_tap(self):
        """
        关闭签到登陆等tab页
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
            print("Tag Close Button Not Found")
            pass

    def check_logined(self):
        """
        检测是否登陆成功
        :return:
        """
        try:
            assert_exists(Template(r"../../imgs/login/play_now_btn.png", record_pos=(-0.001, 0.205),
                                   resolution=(2232, 1080)), "通过PLAY_NOW按钮判断是否登陆")
            return True
        except AssertionError:
            return False

    def logout(self):
        """
        退出游戏并清理缓存
        :return:
        """
        sleep(5)
        clear_app(PACKAGE_NAME)
        stop_app(PACKAGE_NAME)

#
# if __name__ == '__main__':
#     l = LoginView()
#     l.login_as_guest()
