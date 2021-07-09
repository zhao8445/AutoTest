
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
        """
        try:
            position = wait(Template(
                PROJECT_ROOT_PATH + r"/test_view/login_view/imgs/continue_as_guest.png", record_pos=(0.002, 0.196),
                resolution=(1280, 800), threshold=0.7), timeout=60, interval=1)
            touch(position)
            logger.info("点击访客登陆按钮")
        except TargetNotFoundError:
            logger.info("访客登陆按钮未找到")
            pass

    def login_by_account(self, account, password):
        """
        按账号密码登陆
        :param account: 账号
        :param password: 密码
        """
        # 输入账号
        try:
            account_position = wait(
                Template(
                    PROJECT_ROOT_PATH + r"/test_view/login_view/imgs/account_box.png", record_pos=(-0.408, -0.134),
                    resolution=(2232, 1080), threshold=0.9
                ), timeout=60
            )
            touch(account_position)
            sleep(2)
            text(account)
            s = '登陆账号:' + account
            logger.debug(s)
            self.click_confirm_btn()
        except TargetNotFoundError:
            logger.error('未找到account输入框')

        # 输入密码
        try:
            password_position = wait(
                Template(
                    PROJECT_ROOT_PATH + r"/test_view/login_view/imgs/password_box.png", record_pos=(-0.431, -0.073),
                    resolution=(2232, 1080), threshold=0.9
                )
            )
            touch(password_position)
            sleep(3)
            text(password)
            s = '登陆密码:' + password
            logger.debug(s)
            self.click_confirm_btn()
        except TargetNotFoundError:
            logger.error('未找到密码输入框')

        # 点击登录按钮
        login_btn_position = (246, 532)
        sleep(3)
        touch(login_btn_position)

    def click_confirm_btn(self):
        """
        点击小键盘确定按钮
        """
        try:
            confirm_position = wait(
                Template(
                    PROJECT_ROOT_PATH + r"/test_view/login_view/imgs/confirm_btn.png", record_pos=(-0.408, -0.134),
                    resolution=(2232, 1080), threshold=0.9
                ), timeout=4
            )
            touch(confirm_position)
        except TargetNotFoundError:
            logger.error('未找到小键盘确认按钮')

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
        """
        try:
            wait(
                Template(
                    PROJECT_ROOT_PATH + r"/test_view/login_view/imgs/play_now_btn.png", record_pos=(-0.001, 0.205),
                    resolution=(2232, 1080), threshold=0.8
                ), timeout=20, interval=1
            )
            logger.info("---登陆成功---")
            return 1
        except TargetNotFoundError:
            logger.error("---登陆失败---")
            return 0

    def logout(self):
        """
        退出游戏并清理缓存
        :return:
        """
        sleep(5)
        logger.info("---退出游戏---")
        clear_app(PACKAGE_NAME)
        stop_app(PACKAGE_NAME)


lv = LoginView()
