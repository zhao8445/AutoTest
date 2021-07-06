import unittest
from ddt import ddt

from airtest.core.api import *

from test_view.login_view.login_view import LoginView, logger, params

PACKAGE_NAME = params["package_name"]
PROJECT_ROOT_PATH = params["project_root_path"]
USER_DATA_PATH = PROJECT_ROOT_PATH + "/data/user2.json"


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logger.info("execute setUpClass")

    @classmethod
    def tearDownClass(self):
        logger.info("execute tearDownClass")

    def setUp(self):
        pass
        # start_app(PACKAGE_NAME)

        # self.login = LoginView()
        # self.login.login_as_guest()
        # logined = self.login.check_logined()
        # if logined != 1:
        #     for _ in range(3):
        #         self.login.login_as_guest()
        #         logined = self.login.check_logined()
        #         if logined:
        #             break
        # self.assertEqual(logined, 1, "登陆未成功")
        # self.login.close_tap()

    def tearDown(self):
        sleep(5)
        # logger.info("---退出游戏---")
        # logger.info("-------------------------------")
        # clear_app(PACKAGE_NAME)
        # stop_app(PACKAGE_NAME)
