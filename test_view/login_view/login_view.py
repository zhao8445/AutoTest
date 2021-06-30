# -*- encoding=utf8 -*-

__author__ = "zhaobl01"

from base_view.base_view import *

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
            position = wait(Template(
                PROJECT_ROOT_PATH + r"/imgs/login/continue_as_guest.png", record_pos=(0.002, 0.196),
                resolution=(1280, 800), threshold=0.7), timeout=60, interval=1)
            touch(position)
            logger.info("点击访客登陆按钮")
        except TargetNotFoundError:
            logger.info("访客登陆按钮未找到")
            pass

    def close_tap(self):
        """
        关闭签到登陆等tab页
        """
        try:
            position = wait(Template(PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
                                     resolution=(2232, 1080), threshold=0.8), timeout=20, interval=1)
            while position:
                touch(position)
                position = wait(Template(PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
                                         resolution=(2232, 1080), threshold=0.8), timeout=5, interval=1)
        except TargetNotFoundError:
            pass

    def check_logined(self):
        """
        检测是否登陆成功
        :return:
        """
        try:
            assert_exists(Template(PROJECT_ROOT_PATH + r"/imgs/login/play_now_btn.png", record_pos=(-0.001, 0.205),
                                   resolution=(2232, 1080), threshold=0.7), "通过PLAY_NOW按钮判断是否登陆")
            logger.info("---登陆成功---")
            return True
        except AssertionError:
            logger.info("---登陆失败---")
            return False

    def logout(self):
        """
        退出游戏并清理缓存
        :return:
        """
        sleep(5)
        logger.info("---退出游戏---")
        clear_app(PACKAGE_NAME)
        stop_app(PACKAGE_NAME)
